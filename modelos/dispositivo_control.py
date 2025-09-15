# dispositivo_control.py
class DispositivoControl:
    def __init__(self, id_dispositivo_control: int, id_usuario_conectado: int,
                 hora_de_conexion: str, dispositivos_activos: int,
                 dispositivos_apagados: int, dispositivos_en_ahorro: int):
        self._id_dispositivo_control = id_dispositivo_control
        self._id_usuario_conectado = id_usuario_conectado
        self._hora_de_conexion = hora_de_conexion
        self._dispositivos_activos = dispositivos_activos
        self._dispositivos_apagados = dispositivos_apagados
        self._dispositivos_en_ahorro = dispositivos_en_ahorro

    def get_id_dispositivo_control(self) -> int:
        """Devuelve el ID del control de dispositivos"""
        return self._id_dispositivo_control

    def set_dispositivos_activos(self, cantidad: int):
        """Actualiza la cantidad de dispositivos activos"""
        self._dispositivos_activos = cantidad

    def set_dispositivos_apagados(self, cantidad: int):
        """Actualiza la cantidad de dispositivos apagados"""
        self._dispositivos_apagados = cantidad

    def set_dispositivos_en_ahorro(self, cantidad: int):
        """Actualiza la cantidad de dispositivos en modo ahorro"""
        self._dispositivos_en_ahorro = cantidad

    @property
    def dispositivos_activos(self) -> int:
        """Devuelve la cantidad de dispositivos activos"""
        return self._dispositivos_activos

    @property
    def dispositivos_apagados(self) -> int:
        """Devuelve la cantidad de dispositivos apagados"""
        return self._dispositivos_apagados

    @property
    def dispositivos_en_ahorro(self) -> int:
        """Devuelve la cantidad de dispositivos en modo ahorro"""
        return self._dispositivos_en_ahorro
