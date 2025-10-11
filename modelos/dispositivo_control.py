# modelos/dispositivo_control.py  
# Archivo básico para compatibilidad con tests dummy

class DispositivoControl:
    def __init__(self, id_dispositivos_conectados: int, id_usuarios_conectados: int,
                 hora_de_conexion: str, dispositivos_activos: int,
                 dispositivos_apagados: int, dispositivos_en_ahorro: int):
        self._id_dispositivos_conectados = id_dispositivos_conectados
        self._id_usuarios_conectados = id_usuarios_conectados
        self._hora_de_conexion = hora_de_conexion
        self._dispositivos_activos = dispositivos_activos
        self._dispositivos_apagados = dispositivos_apagados
        self._dispositivos_en_ahorro = dispositivos_en_ahorro

    def get_id_dispositivos_conectados(self) -> int:
        return self._id_dispositivos_conectados

    def set_hora_conexion(self, nueva_hora=None) -> None:
        if nueva_hora is not None:
            self._hora_de_conexion = nueva_hora

    def calcular_total_dispositivos(self) -> int:
        return self._dispositivos_activos + self._dispositivos_apagados + self._dispositivos_en_ahorro

    def set_dispositivos_activos(self, cantidad=None):
        if cantidad is not None:
            self._dispositivos_activos = cantidad

    def set_dispositivos_apagados(self, cantidad=None):
        if cantidad is not None:
            self._dispositivos_apagados = cantidad

    def set_dispositivos_en_ahorro(self, cantidad=None):
        if cantidad is not None:
            self._dispositivos_en_ahorro = cantidad

    @property
    def dispositivos_activos(self) -> int:
        return self._dispositivos_activos