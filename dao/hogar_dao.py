from typing import List, Optional, cast
from dominio.hogar import Hogar
from dao.interfaces.i_hogar_dao import IHogarDAO
from connection.obtener_conexion import DatabaseConnection


# Implementación concreta de la interfaz IHogarDAO usando consultas SQL
class HogarDAO(IHogarDAO):

    # Inserta un nuevo hogar en la base de datos
    def crear(self, hogar: Hogar) -> bool:
        query = """
        INSERT INTO hogares (id_hogar, ubicacion, tipo_de_vivienda)
        VALUES (%s, %s, %s)
        """
        try:
            with DatabaseConnection().connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, (
                        int(hogar.id_hogar),
                        str(hogar.ubicacion),
                        str(hogar.tipo_de_vivienda)
                    ))
                    conn.commit()
                    return cursor.rowcount > 0
        except Exception:
            return False

    # Recupera un hogar por su id, devolviendo un objeto Hogar o None
    def leer(self, id_hogar: int) -> Optional[Hogar]:
        query = """
        SELECT ubicacion, tipo_de_vivienda
        FROM hogares
        WHERE id_hogar = %s
        """
        with DatabaseConnection().connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (int(id_hogar),))
                row = cursor.fetchone()
                if row:
                    ubicacion, tipo = row
                    return Hogar(int(id_hogar), str(ubicacion), str(tipo))
                return None

    # Actualiza los datos de un hogar existente
    def actualizar(self, hogar: Hogar) -> bool:
        query = """
        UPDATE hogares
        SET ubicacion = %s, tipo_de_vivienda = %s
        WHERE id_hogar = %s
        """
        try:
            with DatabaseConnection().connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, (
                        str(hogar.ubicacion),
                        str(hogar.tipo_de_vivienda),
                        int(hogar.id_hogar)
                    ))
                    conn.commit()
                    return cursor.rowcount > 0
        except Exception:
            return False

    # Elimina un hogar de la base de datos por id
    def eliminar(self, id_hogar: int) -> bool:
        query = "DELETE FROM hogares WHERE id_hogar = %s"
        try:
            with DatabaseConnection().connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, (int(id_hogar),))
                    conn.commit()
                    return cursor.rowcount > 0
        except Exception:
            return False

    # Obtiene todos los hogares registrados en la base de datos
    def obtener_todos(self) -> List[Hogar]:
        query = """
        SELECT id_hogar, ubicacion, tipo_de_vivienda
        FROM hogares
        """
        hogares: List[Hogar] = []
        with DatabaseConnection().connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                for row in cursor.fetchall():
                    id_hogar, ubicacion, tipo = row
                    hogares.append(Hogar(cast(int, id_hogar),
                                   str(ubicacion), str(tipo)))
        return hogares

    # Verifica si un hogar existe consultando por id
    def existe(self, id_hogar: int) -> bool:
        return self.leer(id_hogar) is not None

    # Obtiene el siguiente id disponible para insertar un nuevo hogar
    def obtener_siguiente_id(self) -> int:
        query = "SELECT COALESCE(MAX(id_hogar), 0) + 1 FROM hogares"
        with DatabaseConnection().connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
                if result is not None:
                    (next_id,) = result
                    return cast(int, next_id)
                return 1
