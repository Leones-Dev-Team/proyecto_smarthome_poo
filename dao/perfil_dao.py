from typing import List, Optional, cast
from dominio.perfil import Perfil
from dao.interfaces.i_perfil_dao import IPerfilDAO
from connection.obtener_conexion import DatabaseConnection


class PerfilDAO(IPerfilDAO):
    def crear(self, perfil: Perfil) -> int:
        query = """
        INSERT INTO perfiles (nombre, mail, telefono, registro_actividad)
        VALUES (%s, %s, %s, %s)
        """
        try:
            perfil.mail = perfil.mail.strip().lower()
            with DatabaseConnection().connect() as conn:
                with conn.cursor(buffered=True) as cursor:
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
                    perfil_id = cursor.lastrowid
                    if not perfil_id:
                        print("No se pudo obtener el ID del perfil.")
                        return 0
                    conn.commit()
                    print("Perfil creado correctamente.")
                    return cast(int, perfil_id)
        except Exception as e:
            print("No se pudo crear el perfil:", e)
            return 0

    def leer(self, id_perfil: int) -> Optional[Perfil]:
        query = "SELECT nombre, mail, telefono, registro_actividad FROM perfiles WHERE id_perfil = %s"
        with DatabaseConnection().connect() as conn:
            with conn.cursor(buffered=True) as cursor:
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
                        perfil.cargar_registro(str(registro))
                    return perfil
                return None

    def actualizar(self, perfil: Perfil, id_perfil: int) -> bool:
        query = """
        UPDATE perfiles
        SET nombre = %s, mail = %s, telefono = %s, registro_actividad = %s
        WHERE id_perfil = %s
        """
        try:
            perfil.mail = perfil.mail.strip().lower()
            with DatabaseConnection().connect() as conn:
                with conn.cursor(buffered=True) as cursor:
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
                    if cursor.rowcount > 0:
                        print("Perfil actualizado correctamente.")
                        return True
                    print("No se encontró el perfil para actualizar.")
                    return False
        except Exception:
            print("No se pudo actualizar el perfil.")
            return False

    def eliminar(self, id_perfil: int) -> bool:
        query = "DELETE FROM perfiles WHERE id_perfil = %s"
        try:
            with DatabaseConnection().connect() as conn:
                with conn.cursor(buffered=True) as cursor:
                    cursor.execute(query, (int(id_perfil),))
                    conn.commit()
                    if cursor.rowcount > 0:
                        print("Perfil eliminado correctamente.")
                        return True
                    print("No se encontró el perfil para eliminar.")
                    return False
        except Exception:
            print("No se pudo eliminar el perfil.")
            return False

    def obtener_todos(self) -> List[Perfil]:
        query = "SELECT id_perfil, nombre, mail, telefono, registro_actividad FROM perfiles"
        perfiles: List[Perfil] = []
        with DatabaseConnection().connect() as conn:
            with conn.cursor(buffered=True) as cursor:
                cursor.execute(query)
                for id_perfil, nombre, mail, telefono, registro in cursor.fetchall():
                    perfil = Perfil(
                        str(nombre),
                        str(mail),
                        str(telefono) if telefono is not None else None,
                        cast(int, id_perfil)
                    )
                    if registro:
                        perfil.cargar_registro(str(registro))
                    perfiles.append(perfil)
        return perfiles
