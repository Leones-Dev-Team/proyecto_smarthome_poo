from typing import List, Optional
from modelos.perfil import Perfil
from dao.i_perfil_dao import IPerfilDAO
from database_connection import obtener_conexion


class PerfilDAO(IPerfilDAO):
    """
    Implementación DAO para la entidad Perfil usando MySQL.
    """

    def crear(self, perfil: Perfil) -> int:
        query = """
        INSERT INTO perfiles (nombre, mail, telefono)
        VALUES (%s, %s, %s)
        """
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (perfil.nombre, perfil.mail, perfil.telefono))
                conn.commit()
                return cursor.lastrowid

    def leer(self, id_perfil: int) -> Optional[Perfil]:
        query = "SELECT nombre, mail, telefono FROM perfiles WHERE id_perfil = %s"
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (id_perfil,))
                row = cursor.fetchone()
                if row:
                    nombre, mail, telefono = row
                    return Perfil(nombre, mail, telefono)
                return None

    def actualizar(self, perfil: Perfil, id_perfil: int) -> bool:
        query = """
        UPDATE perfiles
        SET nombre = %s, mail = %s, telefono = %s
        WHERE id_perfil = %s
        """
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (perfil.nombre, perfil.mail, perfil.telefono, id_perfil))
                conn.commit()
                return cursor.rowcount > 0

    def eliminar(self, id_perfil: int) -> bool:
        query = "DELETE FROM perfiles WHERE id_perfil = %s"
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (id_perfil,))
                conn.commit()
                return cursor.rowcount > 0

    def obtener_todos(self) -> List[Perfil]:
        query = "SELECT nombre, mail, telefono FROM perfiles"
        perfiles = []
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                for nombre, mail, telefono in cursor.fetchall():
                    perfiles.append(Perfil(nombre, mail, telefono))
        return perfiles
