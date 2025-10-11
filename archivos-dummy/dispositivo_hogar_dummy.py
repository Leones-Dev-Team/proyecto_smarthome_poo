# dispositivo_hogar_dummy.py
from typing import Optional


class DispositivoHogar:
    def __init__(self, id_dispositivo: str, id_usuario_conectado: int, ubicacion: str,
                 hora_de_conexion: str, nombre_dispositivo: str, tipo_dispositivo: str,
                 marca_dispositivo: str, consumo_energetico: float, es_esencial: Optional[bool] = False):
        """
        Inicializa un dispositivo del hogar con sus atributos básicos.
        Este dummy no incluye validaciones ni lógica adicional.
        """
        self._id_dispositivo = id_dispositivo
        self._id_usuario_conectado = id_usuario_conectado
        self._ubicacion = ubicacion
        self._hora_de_conexion = hora_de_conexion
        self._nombre_dispositivo = nombre_dispositivo
        self._tipo_dispositivo = tipo_dispositivo
        self._marca_dispositivo = marca_dispositivo
        self._consumo_energetico = consumo_energetico
        self._es_esencial = es_esencial

    def get_id_dispositivo(self) -> str:
        """Devuelve el ID del dispositivo"""
        return self._id_dispositivo
