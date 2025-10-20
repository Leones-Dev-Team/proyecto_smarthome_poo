from typing import List, cast
from dominio.automatizacion import Automatizacion
from dominio.dispositivo_hogar import DispositivoHogar
from dao.interfaces.i_automatizacion_dao import IAutomatizacionDAO
from connection.obtener_conexion import DatabaseConnection


class AutomatizacionDAO(IAutomatizacionDAO):
    def crear(self, automatizacion: Automatizacion) -> int:
        query = "INSERT INTO automatizaciones (nombre) VALUES (%s)"
        try:
            nombre = automatizacion.nombre.strip()
            with DatabaseConnection().connect() as conn:
                with conn.cursor(buffered=True) as cursor:
                    cursor.execute(query, (nombre,))
                    conn.commit()
                    print("Automatización creada correctamente.")
                    return cast(int, cursor.lastrowid)
        except Exception:
            print("No se pudo crear la automatización.")
            return 0

    def leer(self, id_automatizacion: int) -> Automatizacion:
        query = "SELECT nombre FROM automatizaciones WHERE id_automatizacion = %s"
        with DatabaseConnection().connect() as conn:
            with conn.cursor(buffered=True) as cursor:
                cursor.execute(query, (int(id_automatizacion),))
                row = cursor.fetchone()
                if row:
                    (nombre,) = row
                    dispositivos = self.obtener_dispositivos(
                        int(id_automatizacion))
                    return Automatizacion(str(nombre), dispositivos, cast(int, id_automatizacion))
                print("No se encontró la automatización solicitada.")
                raise ValueError("Automatización no encontrada")

    def actualizar(self, automatizacion: Automatizacion) -> bool:
        query = "UPDATE automatizaciones SET nombre = %s WHERE id_automatizacion = %s"
        try:
            nombre = automatizacion.nombre.strip()
            with DatabaseConnection().connect() as conn:
                with conn.cursor(buffered=True) as cursor:
                    cursor.execute(query, (
                        nombre,
                        cast(int, automatizacion.id_automatizacion)
                    ))
                    conn.commit()
                    if cursor.rowcount > 0:
                        print("Automatización actualizada correctamente.")
                        return True
                    print("No se encontró la automatización para actualizar.")
                    return False
        except Exception:
            print("Error al actualizar la automatización.")
            return False

    def eliminar(self, id_automatizacion: int) -> bool:
        query = "DELETE FROM automatizaciones WHERE id_automatizacion = %s"
        try:
            with DatabaseConnection().connect() as conn:
                with conn.cursor(buffered=True) as cursor:
                    cursor.execute(query, (int(id_automatizacion),))
                    conn.commit()
                    if cursor.rowcount > 0:
                        print("Automatización eliminada correctamente.")
                        return True
                    print("No se encontró la automatización para eliminar.")
                    return False
        except Exception:
            print("Error al eliminar la automatización.")
            return False

    def obtener_todos(self) -> List[Automatizacion]:
        query = "SELECT id_automatizacion, nombre FROM automatizaciones"
        automatizaciones: List[Automatizacion] = []
        with DatabaseConnection().connect() as conn:
            with conn.cursor(buffered=True) as cursor:
                cursor.execute(query)
                for row in cursor.fetchall():
                    raw_id_auto, nombre = row
                    dispositivos = self.obtener_dispositivos(
                        cast(int, raw_id_auto))
                    automatizaciones.append(Automatizacion(
                        str(nombre),
                        dispositivos,
                        cast(int, raw_id_auto)
                    ))
        return automatizaciones

    def agregar_dispositivo(self, id_automatizacion: int, id_dispositivo: int) -> bool:
        query = """
        INSERT INTO automatizacion_dispositivo (id_automatizacion, id_dispositivo)
        VALUES (%s, %s)
        """
        try:
            with DatabaseConnection().connect() as conn:
                with conn.cursor(buffered=True) as cursor:
                    cursor.execute(
                        query, (int(id_automatizacion), int(id_dispositivo)))
                    conn.commit()
                    if cursor.rowcount > 0:
                        print("Dispositivo agregado a la automatización.")
                        return True
                    print("No se pudo agregar el dispositivo a la automatización.")
                    return False
        except Exception:
            print("Error al agregar dispositivo a la automatización.")
            return False

    def quitar_dispositivo(self, id_automatizacion: int, id_dispositivo: int) -> bool:
        query = """
        DELETE FROM automatizacion_dispositivo
        WHERE id_automatizacion = %s AND id_dispositivo = %s
        """
        try:
            with DatabaseConnection().connect() as conn:
                with conn.cursor(buffered=True) as cursor:
                    cursor.execute(
                        query, (int(id_automatizacion), int(id_dispositivo)))
                    conn.commit()
                    if cursor.rowcount > 0:
                        print("Dispositivo quitado de la automatización.")
                        return True
                    print("No se encontró el dispositivo en la automatización.")
                    return False
        except Exception:
            print("Error al quitar dispositivo de la automatización.")
            return False

    def obtener_dispositivos(self, id_automatizacion: int) -> List[DispositivoHogar]:
        query = """
        SELECT d.id_dispositivo, d.id_hogar, d.nombre_dispositivo, d.tipo_dispositivo, 
               d.marca_dispositivo, d.estado_dispositivo, d.consumo_energetico, d.es_esencial
        FROM dispositivos_hogar d
        JOIN automatizacion_dispositivo ad ON d.id_dispositivo = ad.id_dispositivo
        WHERE ad.id_automatizacion = %s
        """
        dispositivos: List[DispositivoHogar] = []
        with DatabaseConnection().connect() as conn:
            with conn.cursor(buffered=True) as cursor:
                cursor.execute(query, (int(id_automatizacion),))
                for row in cursor.fetchall():
                    raw_id_disp, raw_id_hogar, nombre, tipo, marca, estado, consumo, es_esencial = row
                    dispositivos.append(DispositivoHogar(
                        cast(int, raw_id_disp),
                        cast(int, raw_id_hogar),
                        str(nombre),
                        str(tipo),
                        str(marca) if marca is not None else None,
                        str(estado),
                        float(cast(float, consumo)),
                        bool(es_esencial)
                    ))
        return dispositivos
