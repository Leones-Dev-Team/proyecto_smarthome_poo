from typing import Optional


class DispositivoControl:
    def __init__(
        self,
        id_dispositivos_conectados: int,
        id_usuarios_conectados: int,
        hora_de_conexion: str,
        dispositivos_activos: int,
        dispositivos_apagados: int,
        dispositivos_en_ahorro: int
    ):
        # Inicializa los atributos básicos del dispositivo de control
        self._id_dispositivos_conectados = id_dispositivos_conectados
        self._id_usuarios_conectados = id_usuarios_conectados
        self._hora_de_conexion = hora_de_conexion
        self._dispositivos_activos = dispositivos_activos
        self._dispositivos_apagados = dispositivos_apagados
        self._dispositivos_en_ahorro = dispositivos_en_ahorro

    def get_id_dispositivos_conectados(self) -> int:
        """Devuelve el ID de los dispositivos conectados."""
        return self._id_dispositivos_conectados

    def set_hora_conexion(self, nueva_hora: Optional[str] = None) -> None:
        """Actualiza la hora de conexión (sin validación en este dummy)."""
        self._hora_de_conexion = nueva_hora or self._hora_de_conexion

    def calcular_total_dispositivos(self) -> int:
        """Calcula y devuelve el total de dispositivos (activos + apagados + en ahorro)."""
        return self._dispositivos_activos + self._dispositivos_apagados + self._dispositivos_en_ahorro

    def set_dispositivos_activos(self, cantidad: Optional[int] = None):
        """Actualiza la cantidad de dispositivos activos (dummy sin validación)."""
        self._dispositivos_activos = cantidad or self._dispositivos_activos

    def set_dispositivos_apagados(self, cantidad: Optional[int] = None):
        """Actualiza la cantidad de dispositivos apagados (dummy sin validación)."""
        self._dispositivos_apagados = cantidad or self._dispositivos_apagados

    def set_dispositivos_en_ahorro(self, cantidad: Optional[int] = None):
        """Actualiza la cantidad de dispositivos en modo ahorro (dummy sin validación)."""
        self._dispositivos_en_ahorro = cantidad or self._dispositivos_en_ahorro

    @property
    def dispositivos_activos(self) -> int:
        """Devuelve la cantidad de dispositivos activos."""
        return self._dispositivos_activos

    @property
    def dispositivos_apagados(self) -> int:
        """Devuelve la cantidad de dispositivos apagados."""
        return self._dispositivos_apagados

    @property
    def dispositivos_en_ahorro(self) -> int:
        """Devuelve la cantidad de dispositivos en modo ahorro."""
        return self._dispositivos_en_ahorro
