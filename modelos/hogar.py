# hogar.py
class Hogar:
    def __init__(self, id_hogar: int, registro_actividad: str, tiempo_de_conexion: str, ubicacion: str, tipo_de_vivienda: str):
        self._id_hogar = id_hogar
        self._registro_actividad = registro_actividad
        self._tiempo_de_conexion = tiempo_de_conexion
        self._ubicacion = ubicacion
        self._tipo_de_vivienda = tipo_de_vivienda

    def get_id_hogar(self) -> int:
        """Devuelve el ID del hogar"""
        return self._id_hogar

    def set_registro_actividad(self, actividad: str):
        """Actualiza el registro de actividad"""
        self._registro_actividad = actividad

    @property
    def registro_actividad(self) -> str:
        """Devuelve el registro de actividad"""
        return self._registro_actividad

    def calcular_tiempo_formateado(self) -> str:
        """Devuelve el tiempo de conexion en formato HH:MM:SS"""
        return self._tiempo_de_conexion
