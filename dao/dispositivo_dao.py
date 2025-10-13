from typing import List, Optional
from modelos.dispositivo_hogar import DispositivoHogar
from dao.i_dispositivo_dao import IDispositivoDAO
from database_connection import obtener_conexion


class DispositivoDAO(IDispositivoDAO):
    def crear(self, dispositivo: DispositivoHogar) -> bool:
        query = """
        INSERT INTO dispositivos (id_dispositivo, nombre, tipo, es_esencial, estado_dispositivo, id_hogar)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (
                    dispositivo.id_dispositivo,
                    dispositivo.nombre,
                    dispositivo.tipo,
                    dispositivo.es_esencial,
                    dispositivo.estado_dispositivo,
                    dispositivo.id_hogar
                ))
                conn.commit()
                return cursor.rowcount > 0

    def leer(self, id_dispositivo: str) -> Optional[DispositivoHogar]:
        query = """
        SELECT nombre, tipo, es_esencial, estado_dispositivo, id_hogar
        FROM dispositivos
        WHERE id_dispositivo = %s
        """
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (id_dispositivo,))
                row = cursor.fetchone()
                if row:
                    nombre, tipo, es_esencial, estado, id_hogar = row
                    dispositivo = DispositivoHogar(id_dispositivo, nombre, tipo, es_esencial, id_hogar)
                    if estado:
                        dispositivo.encender()
                    return dispositivo
                return None

    def actualizar(self, dispositivo: DispositivoHogar) -> bool:
        query = """
        UPDATE dispositivos
        SET nombre = %s, tipo = %s, es_esencial = %s, estado_dispositivo = %s, id_hogar = %s
        WHERE id_dispositivo = %s
        """
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (
                    dispositivo.nombre,
                    dispositivo.tipo,
                    dispositivo.es_esencial,
                    dispositivo.estado_dispositivo,
                    dispositivo.id_hogar,
                    dispositivo.id_dispositivo
                ))
                conn.commit()
                return cursor.rowcount > 0

    def eliminar(self, id_dispositivo: str) -> bool:
        query = "DELETE FROM dispositivos WHERE id_dispositivo = %s"
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (id_dispositivo,))
                conn.commit()
                return cursor.rowcount > 0

    def obtener_todos(self) -> List[DispositivoHogar]:
        query = "SELECT id_dispositivo, nombre, tipo, es_esencial, estado_dispositivo, id_hogar FROM dispositivos"
        dispositivos = []
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                for row in cursor.fetchall():
                    id_disp, nombre, tipo, es_esencial, estado, id_hogar = row
                    dispositivo = DispositivoHogar(id_disp, nombre, tipo, es_esencial, id_hogar)
                    if estado:
                        dispositivo.encender()
                    dispositivos.append(dispositivo)
        return dispositivos

    def listar_por_automatizacion(self, id_automatizacion: int) -> List[DispositivoHogar]:
        query = """
        SELECT d.id_dispositivo, d.nombre, d.tipo, d.es_esencial, d.estado_dispositivo, d.id_hogar
        FROM dispositivos d
        JOIN automatizacion_dispositivo ad ON d.id_dispositivo = ad.id_dispositivo
        WHERE ad.id_automatizacion = %s
        """
        dispositivos = []
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (id_automatizacion,))
                for row in cursor.fetchall():
                    id_disp, nombre, tipo, es_esencial, estado, id_hogar = row
                    dispositivo = DispositivoHogar(id_disp, nombre, tipo, es_esencial, id_hogar)
                    if estado:
                        dispositivo.encender()
                    dispositivos.append(dispositivo)
        return dispositivos

    def actualizar_estado(self, id_dispositivo: str, nuevo_estado: bool) -> bool:
        query = "UPDATE dispositivos SET estado_dispositivo = %s WHERE id_dispositivo = %s"
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (nuevo_estado, id_dispositivo))
                conn.commit()
                return cursor.rowcount > 0
