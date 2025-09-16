class Hogar:
    def __init__(self, id_hogar: int, registro_actividad: str, tiempo_de_conexion: str, ubicacion: str, tipo_de_vivienda: str):
        pass

    def get_id_hogar(self) -> int:
        """Devuelve el ID del hogar"""
        pass

    def set_registro_actividad(self, actividad: str):
        """Actualiza el registro de actividad"""
        pass

    @property
    def registro_actividad(self) -> str:
        """Devuelve el registro de actividad"""
        pass

    def calcular_tiempo_formateado(self) -> str:
        """Devuelve el tiempo de conexion en formato HH:MM:SS"""
        pass