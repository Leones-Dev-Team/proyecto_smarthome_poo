from typing import List, Optional, cast
from dominio.usuario import Usuario
from dominio.perfil import Perfil
from dao.interfaces.i_usuario_dao import IUsuarioDAO
from connection.obtener_conexion import obtener_conexion


class UsuarioDAO(IUsuarioDAO):
    def crear(self, usuario: Usuario) -> bool:
        query = """
        INSERT INTO usuarios (id_usuario, clave, edad, rol, id_hogar, id_perfil)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        try:
            with obtener_conexion() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, (
                        int(usuario.id_usuario),
                        str(usuario._clave),
                        int(usuario.edad),
                        str(usuario.rol),
                        int(usuario.id_hogar),
                        int(usuario.perfil.id_perfil) if usuario.perfil.id_perfil is not None else 0
                    ))
                    conn.commit()
                    return cursor.rowcount > 0
        except Exception:
            return False

    def leer(self, id_usuario: int) -> Optional[Usuario]:
        query = """
        SELECT u.clave, u.edad, u.rol, u.id_hogar, p.id_perfil, p.nombre, p.mail, p.telefono
        FROM usuarios u
        JOIN perfiles p ON u.id_perfil = p.id_perfil
        WHERE u.id_usuario = %s
        """
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (int(id_usuario),))
                row = cursor.fetchone()
                if row:
                    clave, edad, rol, id_hogar, id_perfil, nombre, mail, telefono = row

                    # Forzamos tipos correctos
                    edad = cast(int, edad)
                    id_hogar = cast(int, id_hogar)
                    id_perfil = cast(int, id_perfil)

                    perfil = Perfil(
                        str(nombre),
                        str(mail),
                        str(telefono) if telefono is not None else None,
                        id_perfil
                    )
                    return Usuario(
                        int(id_usuario),
                        str(clave),
                        str(rol),
                        perfil,
                        id_hogar,
                        edad
                    )
                return None

    def actualizar(self, usuario: Usuario) -> bool:
        query = """
        UPDATE usuarios
        SET clave = %s, edad = %s, rol = %s, id_hogar = %s, id_perfil = %s
        WHERE id_usuario = %s
        """
        try:
            with obtener_conexion() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, (
                        str(usuario._clave),
                        int(usuario.edad),
                        str(usuario.rol),
                        int(usuario.id_hogar),
                        int(usuario.perfil.id_perfil) if usuario.perfil.id_perfil is not None else 0,
                        int(usuario.id_usuario)
                    ))
                    conn.commit()
                    return cursor.rowcount > 0
        except Exception:
            return False

    def eliminar(self, id_usuario: int) -> bool:
        query = "DELETE FROM usuarios WHERE id_usuario = %s"
        try:
            with obtener_conexion() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, (int(id_usuario),))
                    conn.commit()
                    return cursor.rowcount > 0
        except Exception:
            return False

    def obtener_todos(self) -> List[Usuario]:
        query = """
        SELECT u.id_usuario, u.clave, u.edad, u.rol, u.id_hogar, p.id_perfil, p.nombre, p.mail, p.telefono
        FROM usuarios u
        JOIN perfiles p ON u.id_perfil = p.id_perfil
        """
        usuarios: List[Usuario] = []
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                for row in cursor.fetchall():
                    id_usuario, clave, edad, rol, id_hogar, id_perfil, nombre, mail, telefono = row

                    # Forzamos tipos correctos
                    id_usuario = cast(int, id_usuario)
                    edad = cast(int, edad)
                    id_hogar = cast(int, id_hogar)
                    id_perfil = cast(int, id_perfil)

                    perfil = Perfil(
                        str(nombre),
                        str(mail),
                        str(telefono) if telefono is not None else None,
                        id_perfil
                    )
                    usuarios.append(Usuario(
                        id_usuario,
                        str(clave),
                        str(rol),
                        perfil,
                        id_hogar,
                        edad
                    ))
        return usuarios
