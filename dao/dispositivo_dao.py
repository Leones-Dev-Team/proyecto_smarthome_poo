from typing import List, Optional, cast
from dominio.dispositivo_hogar import DispositivoHogar
from dao.interfaces.i_dispositivo_dao import IDispositivoDAO
from connection.obtener_conexion import DatabaseConnection
from dao.hogar_dao import HogarDAO


class DispositivoDAO(IDispositivoDAO):
    def crear(self, dispositivo: DispositivoHogar) -> bool:
        if not HogarDAO().existe(dispositivo.id_hogar):
            print("El hogar seleccionado no existe.")
            return False
        query = """
        INSERT INTO dispositivos_hogar (id_dispositivo, id_hogar, nombre_dispositivo, tipo_dispositivo, 
                                       marca_dispositivo, estado_dispositivo, consumo_energetico, es_esencial)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        try:
            nombre = dispositivo.nombre.strip()
            tipo = dispositivo.tipo.strip()
            marca = dispositivo.marca.strip() if dispositivo.marca else None
            estado = dispositivo.estado_dispositivo.strip()
            with DatabaseConnection().connect() as conn:
                with conn.cursor(buffered=True) as cursor:
                    cursor.execute(query, (
                        int(dispositivo.id_dispositivo),
                        int(dispositivo.id_hogar),
                        nombre,
                        tipo,
                        marca,
                        estado,
                        float(dispositivo.consumo_energetico),
                        bool(dispositivo.es_esencial)
                    ))
                    conn.commit()
                    if cursor.rowcount > 0:
                        print("Dispositivo creado correctamente.")
                        return True
                    print("No se pudo crear el dispositivo.")
                    return False
        except Exception:
            print("Error al crear el dispositivo.")
            return False

    def leer(self, id_dispositivo: int) -> Optional[DispositivoHogar]:
        query = """
        SELECT id_hogar, nombre_dispositivo, tipo_dispositivo, marca_dispositivo, 
               estado_dispositivo, consumo_energetico, es_esencial
        FROM dispositivos_hogar
        WHERE id_dispositivo = %s
        """
        with DatabaseConnection().connect() as conn:
            with conn.cursor(buffered=True) as cursor:
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
                print("No se encontró el dispositivo solicitado.")
                return None

    def actualizar(self, dispositivo: DispositivoHogar) -> bool:
        query = """
        UPDATE dispositivos_hogar
        SET id_hogar = %s, nombre_dispositivo = %s, tipo_dispositivo = %s, marca_dispositivo = %s, 
            estado_dispositivo = %s, consumo_energetico = %s, es_esencial = %s
        WHERE id_dispositivo = %s
        """
        try:
            nombre = dispositivo.nombre.strip()
            tipo = dispositivo.tipo.strip()
            marca = dispositivo.marca.strip() if dispositivo.marca else None
            estado = dispositivo.estado_dispositivo.strip()
            with DatabaseConnection().connect() as conn:
                with conn.cursor(buffered=True) as cursor:
                    cursor.execute(query, (
                        int(dispositivo.id_hogar),
                        nombre,
                        tipo,
                        marca,
                        estado,
                        float(dispositivo.consumo_energetico),
                        bool(dispositivo.es_esencial),
                        int(dispositivo.id_dispositivo)
                    ))
                    conn.commit()
                    if cursor.rowcount > 0:
                        print("Dispositivo actualizado correctamente.")
                        return True
                    print("No se encontró el dispositivo para actualizar.")
                    return False
        except Exception:
            print("Error al actualizar el dispositivo.")
            return False

    def eliminar(self, id_dispositivo: int) -> bool:
        query = "DELETE FROM dispositivos_hogar WHERE id_dispositivo = %s"
        try:
            with DatabaseConnection().connect() as conn:
                with conn.cursor(buffered=True) as cursor:
                    cursor.execute(query, (int(id_dispositivo),))
                    conn.commit()
                    if cursor.rowcount > 0:
                        print("Dispositivo eliminado correctamente.")
                        return True
                    print("No se encontró el dispositivo para eliminar.")
                    return False
        except Exception:
            print("Error al eliminar el dispositivo.")
            return False

    def obtener_todos(self) -> List[DispositivoHogar]:
        query = """
        SELECT id_dispositivo, id_hogar, nombre_dispositivo, tipo_dispositivo, 
               marca_dispositivo, estado_dispositivo, consumo_energetico, es_esencial 
        FROM dispositivos_hogar
        """
        dispositivos: List[DispositivoHogar] = []
        with DatabaseConnection().connect() as conn:
            with conn.cursor(buffered=True) as cursor:
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

    def listar_por_hogar(self, id_hogar: int) -> List[DispositivoHogar]:
        query = """
        SELECT id_dispositivo, id_hogar, nombre_dispositivo, tipo_dispositivo, 
               marca_dispositivo, estado_dispositivo, consumo_energetico, es_esencial
        FROM dispositivos_hogar
        WHERE id_hogar = %s
        """
        dispositivos: List[DispositivoHogar] = []
        with DatabaseConnection().connect() as conn:
            with conn.cursor(buffered=True) as cursor:
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
        with DatabaseConnection().connect() as conn:
            with conn.cursor(buffered=True) as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
                if result is not None:
                    (next_id,) = result
                    return cast(int, next_id)
                return 1
