from typing import List, Optional, cast
from dominio.usuario import Usuario
from dominio.perfil import Perfil
from dao.interfaces.i_usuario_dao import IUsuarioDAO
from connection.obtener_conexion import DatabaseConnection
from dao.hogar_dao import HogarDAO
from dao.perfil_dao import PerfilDAO
import mysql.connector


class UsuarioDAO(IUsuarioDAO):
    def crear(self, usuario: Usuario) -> bool:
        if not HogarDAO().existe(usuario.id_hogar):
            print("El hogar seleccionado no existe.")
            return False

        # Normalizar correo
        usuario.perfil.mail = usuario.perfil.mail.strip().lower()

        query_check_usuario = "SELECT 1 FROM usuarios WHERE id_usuario = %s"
        query_usuario = """
        INSERT INTO usuarios (id_usuario, clave, edad, rol, id_hogar, id_perfil)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        try:
            with DatabaseConnection().connect() as conn:
                # Validar id_usuario duplicado
                with conn.cursor(buffered=True) as cursor:
                    cursor.execute(query_check_usuario, (usuario.id_usuario,))
                    if cursor.fetchone() is not None:
                        print("Ya existe un usuario con ese ID.")
                        return False

                # Crear perfil primero usando PerfilDAO
                perfil_id = PerfilDAO().crear(usuario.perfil)
                if not perfil_id:
                    print("No se pudo generar el perfil.")
                    return False
                usuario.perfil.id_perfil = perfil_id

                # Insertar usuario
                try:
                    with conn.cursor(buffered=True) as cursor:
                        cursor.execute(query_usuario, (
                            int(usuario.id_usuario),
                            usuario.clave,
                            int(usuario.edad),
                            str(usuario.rol),
                            int(usuario.id_hogar),
                            usuario.perfil.id_perfil
                        ))
                    conn.commit()
                    print("Usuario registrado correctamente.")
                    return True
                except Exception as e:
                    PerfilDAO().eliminar(usuario.perfil.id_perfil)
                    conn.commit()
                    print("Error al registrar usuario, perfil eliminado:", e)
                    return False

        except mysql.connector.errors.IntegrityError as e:
            if e.errno == 1062:
                print("Ya existe un usuario con esos datos.")
                return False
            print("Error de integridad en la base de datos.")
            return False
        except Exception as e:
            print("Ocurrió un error al registrar el usuario:", e)
            return False

    def leer(self, id_usuario: int) -> Optional[Usuario]:
        query = """
        SELECT u.clave, u.edad, u.rol, u.id_hogar, p.id_perfil, p.nombre, p.mail, p.telefono
        FROM usuarios u
        JOIN perfiles p ON u.id_perfil = p.id_perfil
        WHERE u.id_usuario = %s
        """
        with DatabaseConnection().connect() as conn:
            with conn.cursor(buffered=True) as cursor:
                cursor.execute(query, (int(id_usuario),))
                row = cursor.fetchone()
                if row:
                    clave, edad, rol, id_hogar, id_perfil, nombre, mail, telefono = row
                    perfil = Perfil(
                        str(nombre),
                        str(mail),
                        str(telefono) if telefono is not None else None,
                        cast(int, id_perfil)
                    )
                    return Usuario(
                        int(id_usuario),
                        str(clave),
                        str(rol),
                        perfil,
                        cast(int, id_hogar),
                        cast(int, edad)
                    )
                return None

    def actualizar(self, usuario: Usuario) -> bool:
        query = """
        UPDATE usuarios
        SET clave = %s, edad = %s, rol = %s, id_hogar = %s
        WHERE id_usuario = %s
        """
        try:
            with DatabaseConnection().connect() as conn:
                with conn.cursor(buffered=True) as cursor:
                    cursor.execute(query, (
                        usuario.clave,
                        int(usuario.edad),
                        str(usuario.rol),
                        int(usuario.id_hogar),
                        int(usuario.id_usuario)
                    ))
                    conn.commit()
                    return cursor.rowcount > 0
        except Exception:
            return False

    def eliminar(self, id_usuario: int) -> bool:
        query = "DELETE FROM usuarios WHERE id_usuario = %s"
        try:
            with DatabaseConnection().connect() as conn:
                with conn.cursor(buffered=True) as cursor:
                    cursor.execute(query, (int(id_usuario),))
                    conn.commit()
                    return cursor.rowcount > 0
        except Exception:
            return False

    def obtener_todos(self) -> List[Usuario]:
        query = """
        SELECT u.id_usuario, u.clave, u.edad, u.rol, u.id_hogar,
               p.id_perfil, p.nombre, p.mail, p.telefono
        FROM usuarios u
        JOIN perfiles p ON u.id_perfil = p.id_perfil
        """
        usuarios: List[Usuario] = []
        with DatabaseConnection().connect() as conn:
            with conn.cursor(buffered=True) as cursor:
                cursor.execute(query)
                for row in cursor.fetchall():
                    id_usuario, clave, edad, rol, id_hogar, id_perfil, nombre, mail, telefono = row
                    perfil = Perfil(
                        str(nombre),
                        str(mail),
                        str(telefono) if telefono is not None else None,
                        cast(int, id_perfil)
                    )
                    usuarios.append(Usuario(
                        cast(int, id_usuario),
                        str(clave),
                        str(rol),
                        perfil,
                        cast(int, id_hogar),
                        cast(int, edad)
                    ))
        return usuarios

    def leer_por_email(self, email: str) -> Optional[Usuario]:
        query = """
        SELECT u.id_usuario, u.clave, u.edad, u.rol, u.id_hogar,
               p.id_perfil, p.nombre, p.mail, p.telefono
        FROM usuarios u
        JOIN perfiles p ON u.id_perfil = p.id_perfil
        WHERE p.mail = %s
        """
        with DatabaseConnection().connect() as conn:
            with conn.cursor(buffered=True) as cursor:
                cursor.execute(query, (email.strip().lower(),))
                row = cursor.fetchone()
                if row:
                    id_usuario, clave, edad, rol, id_hogar, id_perfil, nombre, mail, telefono = row
                    perfil = Perfil(
                        str(nombre),
                        str(mail),
                        str(telefono) if telefono is not None else None,
                        cast(int, id_perfil)
                    )
                    return Usuario(
                        cast(int, id_usuario),
                        str(clave),
                        str(rol),
                        perfil,
                        cast(int, id_hogar),
                        cast(int, edad)
                    )
                return None

    def obtener_siguiente_id(self) -> int:
        query = "SELECT COALESCE(MAX(id_usuario), 0) + 1 FROM usuarios"
        with DatabaseConnection().connect() as conn:
            with conn.cursor(buffered=True) as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
                if result is not None:
                    (next_id,) = result
                    return cast(int, next_id)
                return 1
