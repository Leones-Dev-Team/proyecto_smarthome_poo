# hogar_dummy.py
from typing import Optional


class Hogar:
    def __init__(self, id_hogar: int, registro_actividad: str,
                 tiempo_de_conexion: str, ubicacion: str, tipo_de_vivienda: str):
        """
        Inicializa un hogar con sus atributos básicos.
        Este dummy no incluye validaciones ni lógica adicional.
        """
        self._id_hogar = id_hogar
        self._registro_actividad = registro_actividad
        self._tiempo_de_conexion = tiempo_de_conexion
        self._ubicacion = ubicacion
        self._tipo_de_vivienda = tipo_de_vivienda

    def get_id_hogar(self) -> int:
        """Devuelve el ID del hogar"""
        return self._id_hogar

    def set_registro_actividad(self, actividad: Optional[str] = None):
        """Actualiza el registro de actividad"""
        if actividad is not None:
            self._registro_actividad = actividad

    @property
    def registro_actividad(self) -> str:
        """Devuelve el registro de actividad"""
        return self._registro_actividad

    def calcular_tiempo_formateado(self) -> str:
        """Devuelve el tiempo de conexión en formato HH:MM:SS (dummy sin validación)"""
        return self._tiempo_de_conexion
