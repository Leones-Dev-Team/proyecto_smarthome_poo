from typing import List
from modelos.automatizacion import Automatizacion
from modelos.dispositivo_hogar import DispositivoHogar
from dao.i_automatizacion_dao import IAutomatizacionDAO
from database_connection import obtener_conexion


class AutomatizacionDAO(IAutomatizacionDAO):
    """
    Implementación DAO para la entidad Automatizacion y su relación con dispositivos.
    """

    def crear(self, automatizacion: Automatizacion) -> int:
        query = "INSERT INTO automatizaciones (nombre) VALUES (%s)"
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (automatizacion.nombre,))
                conn.commit()
                return cursor.lastrowid

    def leer(self, id_automatizacion: int) -> Automatizacion:
        query = "SELECT nombre FROM automatizaciones WHERE id_automatizacion = %s"
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (id_automatizacion,))
                row = cursor.fetchone()
                if row:
                    nombre = row[0]
                    dispositivos = self.obtener_dispositivos(id_automatizacion)
                    return Automatizacion(nombre, dispositivos)
                raise ValueError("Automatización no encontrada")

    def actualizar(self, automatizacion: Automatizacion, id_automatizacion: int) -> bool:
        query = "UPDATE automatizaciones SET nombre = %s WHERE id_automatizacion = %s"
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (automatizacion.nombre, id_automatizacion))
                conn.commit()
                return cursor.rowcount > 0

    def eliminar(self, id_automatizacion: int) -> bool:
        query = "DELETE FROM automatizaciones WHERE id_automatizacion = %s"
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (id_automatizacion,))
                conn.commit()
                return cursor.rowcount > 0

    def obtener_todos(self) -> List[Automatizacion]:
        query = "SELECT id_automatizacion, nombre FROM automatizaciones"
        automatizaciones = []
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                for id_auto, nombre in cursor.fetchall():
                    dispositivos = self.obtener_dispositivos(id_auto)
                    automatizaciones.append(Automatizacion(nombre, dispositivos))
        return automatizaciones

    def agregar_dispositivo(self, id_automatizacion: int, id_dispositivo: str) -> bool:
        query = """
        INSERT INTO automatizacion_dispositivo (id_automatizacion, id_dispositivo)
        VALUES (%s, %s)
        """
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (id_automatizacion, id_dispositivo))
                conn.commit()
                return cursor.rowcount > 0

    def quitar_dispositivo(self, id_automatizacion: int, id_dispositivo: str) -> bool:
        query = """
        DELETE FROM automatizacion_dispositivo
        WHERE id_automatizacion = %s AND id_dispositivo = %s
        """
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (id_automatizacion, id_dispositivo))
                conn.commit()
                return cursor.rowcount > 0

    def obtener_dispositivos(self, id_automatizacion: int) -> List[DispositivoHogar]:
        query = """
        SELECT d.id_dispositivo, d.nombre, d.tipo, d.es_esencial, d.estado_dispositivo
        FROM dispositivos d
        JOIN automatizacion_dispositivo ad ON d.id_dispositivo = ad.id_dispositivo
        WHERE ad.id_automatizacion = %s
        """
        dispositivos = []
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (id_automatizacion,))
                for row in cursor.fetchall():
                    id_disp, nombre, tipo, es_esencial, estado = row
                    dispositivo = DispositivoHogar(id_disp, nombre, tipo, es_esencial)
                    if estado:
                        dispositivo.encender()
                    dispositivos.append(dispositivo)
        return dispositivos
