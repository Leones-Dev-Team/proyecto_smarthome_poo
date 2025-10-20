from typing import List, Optional, cast
from dominio.hogar import Hogar
from dao.interfaces.i_hogar_dao import IHogarDAO
from connection.obtener_conexion import DatabaseConnection


class HogarDAO(IHogarDAO):

    def crear(self, hogar: Hogar) -> bool:
        query = """
        INSERT INTO hogares (id_hogar, ubicacion, tipo_de_vivienda)
        VALUES (%s, %s, %s)
        """
        try:
            ubicacion = hogar.ubicacion.strip()
            tipo = hogar.tipo_de_vivienda.strip()
            with DatabaseConnection().connect() as conn:
                with conn.cursor(buffered=True) as cursor:
                    cursor.execute(query, (
                        int(hogar.id_hogar),
                        ubicacion,
                        tipo
                    ))
                    conn.commit()
                    if cursor.rowcount > 0:
                        print("Hogar creado correctamente.")
                        return True
                    print("No se pudo crear el hogar.")
                    return False
        except Exception:
            print("Error al crear el hogar.")
            return False

    def leer(self, id_hogar: int) -> Optional[Hogar]:
        query = """
        SELECT ubicacion, tipo_de_vivienda
        FROM hogares
        WHERE id_hogar = %s
        """
        with DatabaseConnection().connect() as conn:
            with conn.cursor(buffered=True) as cursor:
                cursor.execute(query, (int(id_hogar),))
                row = cursor.fetchone()
                if row:
                    ubicacion, tipo = row
                    return Hogar(int(id_hogar), str(ubicacion), str(tipo))
                print("No se encontró el hogar solicitado.")
                return None

    def actualizar(self, hogar: Hogar) -> bool:
        query = """
        UPDATE hogares
        SET ubicacion = %s, tipo_de_vivienda = %s
        WHERE id_hogar = %s
        """
        try:
            ubicacion = hogar.ubicacion.strip()
            tipo = hogar.tipo_de_vivienda.strip()
            with DatabaseConnection().connect() as conn:
                with conn.cursor(buffered=True) as cursor:
                    cursor.execute(query, (
                        ubicacion,
                        tipo,
                        int(hogar.id_hogar)
                    ))
                    conn.commit()
                    if cursor.rowcount > 0:
                        print("Hogar actualizado correctamente.")
                        return True
                    print("No se encontró el hogar para actualizar.")
                    return False
        except Exception:
            print("Error al actualizar el hogar.")
            return False

    def eliminar(self, id_hogar: int) -> bool:
        query = "DELETE FROM hogares WHERE id_hogar = %s"
        try:
            with DatabaseConnection().connect() as conn:
                with conn.cursor(buffered=True) as cursor:
                    cursor.execute(query, (int(id_hogar),))
                    conn.commit()
                    if cursor.rowcount > 0:
                        print("Hogar eliminado correctamente.")
                        return True
                    print("No se encontró el hogar para eliminar.")
                    return False
        except Exception:
            print("Error al eliminar el hogar.")
            return False

    def obtener_todos(self) -> List[Hogar]:
        query = """
        SELECT id_hogar, ubicacion, tipo_de_vivienda
        FROM hogares
        """
        hogares: List[Hogar] = []
        with DatabaseConnection().connect() as conn:
            with conn.cursor(buffered=True) as cursor:
                cursor.execute(query)
                for row in cursor.fetchall():
                    id_hogar, ubicacion, tipo = row
                    hogares.append(Hogar(
                        cast(int, id_hogar),
                        str(ubicacion),
                        str(tipo)
                    ))
        return hogares

    def existe(self, id_hogar: int) -> bool:
        return self.leer(id_hogar) is not None

    def obtener_siguiente_id(self) -> int:
        query = "SELECT COALESCE(MAX(id_hogar), 0) + 1 FROM hogares"
        with DatabaseConnection().connect() as conn:
            with conn.cursor(buffered=True) as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
                if result is not None:
                    (next_id,) = result
                    return cast(int, next_id)
                return 1
