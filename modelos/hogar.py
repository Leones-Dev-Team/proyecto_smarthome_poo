# modelos/hogar.py
# Archivo básico para compatibilidad con tests dummy

class Hogar:
    def __init__(self, id_hogar: int, registro_actividad: str,
                 tiempo_de_conexion: str, ubicacion: str, tipo_de_vivienda: str):
        self._id_hogar = id_hogar
        self._registro_actividad = registro_actividad
        self._tiempo_de_conexion = tiempo_de_conexion
        self._ubicacion = ubicacion
        self._tipo_de_vivienda = tipo_de_vivienda

    def get_id_hogar(self) -> int:
        return self._id_hogar

    def set_registro_actividad(self, actividad=None):
        if actividad is not None:
            self._registro_actividad = actividad

    @property
    def registro_actividad(self) -> str:
        return self._registro_actividad

    def calcular_tiempo_formateado(self) -> str:
        return self._tiempo_de_conexion