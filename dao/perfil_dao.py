from typing import List, Optional, cast
from dominio.perfil import Perfil
from dao.interfaces.i_perfil_dao import IPerfilDAO
from connection.obtener_conexion import DatabaseConnection


class PerfilDAO(IPerfilDAO):
    # Inserta un nuevo perfil en la base de datos y devuelve su id generado
    def crear(self, perfil: Perfil) -> int:
        query = """
        INSERT INTO perfiles (nombre, mail, telefono, registro_actividad)
        VALUES (%s, %s, %s, %s)
        """
        try:
            with DatabaseConnection().connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        query,
                        (
                            str(perfil.nombre),
                            str(perfil.mail),
                            str(perfil.telefono) if perfil.telefono is not None else None,
                            ", ".join(
                                perfil.registro_actividad) if perfil.registro_actividad else ""
                        )
                    )
                    conn.commit()
                    return cast(int, cursor.lastrowid)
        except Exception:
            raise

    # Recupera un perfil por su id, devolviendo None si no existe
    def leer(self, id_perfil: int) -> Optional[Perfil]:
        query = "SELECT nombre, mail, telefono, registro_actividad FROM perfiles WHERE id_perfil = %s"
        with DatabaseConnection().connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (int(id_perfil),))
                row = cursor.fetchone()
                if row:
                    nombre, mail, telefono, registro = row
                    perfil = Perfil(
                        str(nombre),
                        str(mail),
                        str(telefono) if telefono is not None else None,
                        int(id_perfil)
                    )
                    if registro:
                        perfil._registro_actividad = str(registro).split(", ")
                    return perfil
                return None

    # Actualiza los datos de un perfil existente, devolviendo True si se modificó
    def actualizar(self, perfil: Perfil, id_perfil: int) -> bool:
        query = """
        UPDATE perfiles
        SET nombre = %s, mail = %s, telefono = %s, registro_actividad = %s
        WHERE id_perfil = %s
        """
        try:
            with DatabaseConnection().connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        query,
                        (
                            str(perfil.nombre),
                            str(perfil.mail),
                            str(perfil.telefono) if perfil.telefono is not None else None,
                            ", ".join(
                                perfil.registro_actividad) if perfil.registro_actividad else "",
                            int(id_perfil)
                        )
                    )
                    conn.commit()
                    return cursor.rowcount > 0
        except Exception:
            return False

    # Elimina un perfil por su id, devolviendo True si se borró
    def eliminar(self, id_perfil: int) -> bool:
        query = "DELETE FROM perfiles WHERE id_perfil = %s"
        try:
            with DatabaseConnection().connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, (int(id_perfil),))
                    conn.commit()
                    return cursor.rowcount > 0
        except Exception:
            return False

    # Devuelve la lista completa de perfiles almacenados en la base de datos
    def obtener_todos(self) -> List[Perfil]:
        query = "SELECT id_perfil, nombre, mail, telefono, registro_actividad FROM perfiles"
        perfiles: List[Perfil] = []
        with DatabaseConnection().connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                for id_perfil, nombre, mail, telefono, registro in cursor.fetchall():
                    perfil = Perfil(
                        str(nombre),
                        str(mail),
                        str(telefono) if telefono is not None else None,
                        cast(int, id_perfil)
                    )
                    if registro:
                        perfil._registro_actividad = str(registro).split(", ")
                    perfiles.append(perfil)
        return perfiles
