from typing import List, Optional
from modelos.usuario import Usuario
from modelos.perfil import Perfil
from dao.i_usuario_dao import IUsuarioDAO
from database_connection import obtener_conexion


class UsuarioDAO(IUsuarioDAO):
    def crear(self, usuario: Usuario) -> bool:
        query = """
        INSERT INTO usuarios (id_usuario, contrasena, rol, id_perfil, id_hogar)
        VALUES (%s, %s, %s, %s, %s)
        """
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (
                    usuario.id_usuario,
                    usuario.contrasena,
                    usuario.rol,
                    usuario.id_perfil,
                    usuario.id_hogar
                ))
                conn.commit()
                return cursor.rowcount > 0

    def leer(self, id_usuario: int) -> Optional[Usuario]:
        query = """
        SELECT contrasena, rol, id_perfil, id_hogar
        FROM usuarios
        WHERE id_usuario = %s
        """
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (id_usuario,))
                row = cursor.fetchone()
                if row:
                    contrasena, rol, id_perfil, id_hogar = row
                    perfil = Perfil("", "") if id_perfil else None  # Placeholder
                    return Usuario(id_usuario, contrasena, rol, perfil, id_hogar)
                return None

    def actualizar(self, usuario: Usuario) -> bool:
        query = """
        UPDATE usuarios
        SET contrasena = %s, rol = %s, id_perfil = %s, id_hogar = %s
        WHERE id_usuario = %s
        """
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (
                    usuario.contrasena,
                    usuario.rol,
                    usuario.id_perfil,
                    usuario.id_hogar,
                    usuario.id_usuario
                ))
                conn.commit()
                return cursor.rowcount > 0

    def eliminar(self, id_usuario: int) -> bool:
        query = "DELETE FROM usuarios WHERE id_usuario = %s"
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (id_usuario,))
                conn.commit()
                return cursor.rowcount > 0

    def obtener_todos(self) -> List[Usuario]:
        query = "SELECT id_usuario, contrasena, rol, id_perfil, id_hogar FROM usuarios"
        usuarios = []
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                for row in cursor.fetchall():
                    id_usuario, contrasena, rol, id_perfil, id_hogar = row
                    perfil = Perfil("", "") if id_perfil else None
                    usuarios.append(Usuario(id_usuario, contrasena, rol, perfil, id_hogar))
        return usuarios

    def asociar_perfil(self, id_usuario: int, id_perfil: int) -> bool:
        query = "UPDATE usuarios SET id_perfil = %s WHERE id_usuario = %s"
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (id_perfil, id_usuario))
                conn.commit()
                return cursor.rowcount > 0

    def desasociar_perfil(self, id_usuario: int) -> bool:
        query = "UPDATE usuarios SET id_perfil = NULL WHERE id_usuario = %s"
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (id_usuario,))
                conn.commit()
                return cursor.rowcount > 0

    def asignar_hogar(self, id_usuario: int, id_hogar: int) -> bool:
        query = "UPDATE usuarios SET id_hogar = %s WHERE id_usuario = %s"
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (id_hogar, id_usuario))
                conn.commit()
                return cursor.rowcount > 0

    def quitar_hogar(self, id_usuario: int) -> bool:
        query = "UPDATE usuarios SET id_hogar = NULL WHERE id_usuario = %s"
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (id_usuario,))
                conn.commit()
                return cursor.rowcount > 0
