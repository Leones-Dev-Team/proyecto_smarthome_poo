from typing import List, Optional, cast
from dominio.dispositivo_hogar import DispositivoHogar
from dao.interfaces.i_dispositivo_dao import IDispositivoDAO
from connection.obtener_conexion import obtener_conexion
from dao.hogar_dao import HogarDAO


class DispositivoDAO(IDispositivoDAO):
    # Inserta un nuevo dispositivo en la base de datos
    def crear(self, dispositivo: DispositivoHogar) -> bool:
        if not HogarDAO().existe(dispositivo.id_hogar):
            raise ValueError("El hogar no existe.")
        query = """
        INSERT INTO dispositivos_hogar (id_dispositivo, id_hogar, nombre_dispositivo, tipo_dispositivo, 
                                       marca_dispositivo, estado_dispositivo, consumo_energetico, es_esencial)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        try:
            with obtener_conexion() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, (
                        int(dispositivo.id_dispositivo),
                        int(dispositivo.id_hogar),
                        str(dispositivo.nombre),
                        str(dispositivo.tipo),
                        str(dispositivo.marca) if dispositivo.marca is not None else None,
                        str(dispositivo.estado_dispositivo),
                        float(dispositivo.consumo_energetico),
                        bool(dispositivo.es_esencial)
                    ))
                    conn.commit()
                    return cursor.rowcount > 0
        except Exception:
            return False

    # Recupera un dispositivo por su id
    def leer(self, id_dispositivo: int) -> Optional[DispositivoHogar]:
        query = """
        SELECT id_hogar, nombre_dispositivo, tipo_dispositivo, marca_dispositivo, 
               estado_dispositivo, consumo_energetico, es_esencial
        FROM dispositivos_hogar
        WHERE id_dispositivo = %s
        """
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (int(id_dispositivo),))
                row = cursor.fetchone()
                if row:
                    raw_id_hogar, nombre, tipo, marca, estado, consumo, es_esencial = row
                    return DispositivoHogar(
                        int(id_dispositivo),
                        cast(int, raw_id_hogar),
                        str(nombre),
                        str(tipo),
                        str(marca) if marca is not None else None,
                        str(estado),
                        float(cast(float, consumo)),
                        bool(es_esencial)
                    )
                return None

    # Actualiza los datos de un dispositivo existente
    def actualizar(self, dispositivo: DispositivoHogar) -> bool:
        query = """
        UPDATE dispositivos_hogar
        SET id_hogar = %s, nombre_dispositivo = %s, tipo_dispositivo = %s, marca_dispositivo = %s, 
            estado_dispositivo = %s, consumo_energetico = %s, es_esencial = %s
        WHERE id_dispositivo = %s
        """
        try:
            with obtener_conexion() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, (
                        int(dispositivo.id_hogar),
                        str(dispositivo.nombre),
                        str(dispositivo.tipo),
                        str(dispositivo.marca) if dispositivo.marca is not None else None,
                        str(dispositivo.estado_dispositivo),
                        float(dispositivo.consumo_energetico),
                        bool(dispositivo.es_esencial),
                        int(dispositivo.id_dispositivo)
                    ))
                    conn.commit()
                    return cursor.rowcount > 0
        except Exception:
            return False

    # Elimina un dispositivo por su id
    def eliminar(self, id_dispositivo: int) -> bool:
        query = "DELETE FROM dispositivos_hogar WHERE id_dispositivo = %s"
        try:
            with obtener_conexion() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, (int(id_dispositivo),))
                    conn.commit()
                    return cursor.rowcount > 0
        except Exception:
            return False

    # Devuelve todos los dispositivos registrados
    def obtener_todos(self) -> List[DispositivoHogar]:
        query = """
        SELECT id_dispositivo, id_hogar, nombre_dispositivo, tipo_dispositivo, 
               marca_dispositivo, estado_dispositivo, consumo_energetico, es_esencial 
        FROM dispositivos_hogar
        """
        dispositivos: List[DispositivoHogar] = []
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                for row in cursor.fetchall():
                    raw_id_dispositivo, raw_id_hogar, nombre, tipo, marca, estado, consumo, es_esencial = row
                    dispositivos.append(DispositivoHogar(
                        cast(int, raw_id_dispositivo),
                        cast(int, raw_id_hogar),
                        str(nombre),
                        str(tipo),
                        str(marca) if marca is not None else None,
                        str(estado),
                        float(cast(float, consumo)),
                        bool(es_esencial)
                    ))
        return dispositivos

    # Lista todos los dispositivos de un hogar específico
    def listar_por_hogar(self, id_hogar: int) -> List[DispositivoHogar]:
        query = """
        SELECT id_dispositivo, id_hogar, nombre_dispositivo, tipo_dispositivo, 
               marca_dispositivo, estado_dispositivo, consumo_energetico, es_esencial
        FROM dispositivos_hogar
        WHERE id_hogar = %s
        """
        dispositivos: List[DispositivoHogar] = []
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (int(id_hogar),))
                for row in cursor.fetchall():
                    raw_id_dispositivo, raw_id_hogar, nombre, tipo, marca, estado, consumo, es_esencial = row
                    dispositivos.append(DispositivoHogar(
                        cast(int, raw_id_dispositivo),
                        cast(int, raw_id_hogar),
                        str(nombre),
                        str(tipo),
                        str(marca) if marca is not None else None,
                        str(estado),
                        float(cast(float, consumo)),
                        bool(es_esencial)
                    ))
        return dispositivos

    def obtener_siguiente_id(self) -> int:
        query = "SELECT COALESCE(MAX(id_dispositivo), 0) + 1 FROM dispositivos_hogar"
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
                if result is not None:
                    (next_id,) = result
                    return cast(int, next_id)
                return 1
