from __future__ import annotations


class DispositivoControl:
    """
    Representa un dispositivo de control en el sistema SmartHome.
    """

    def __init__(self, id_dispositivo_control: int, id_usuario: int, hora_de_conexion: str,
                 dispositivos_activos: int, dispositivos_apagados: int, dispositivos_en_ahorro: int):
        self._id_dispositivo_control = id_dispositivo_control
        self._id_usuario = id_usuario
        self._hora_de_conexion = hora_de_conexion
        self._dispositivos_activos = dispositivos_activos
        self._dispositivos_apagados = dispositivos_apagados
        self._dispositivos_en_ahorro = dispositivos_en_ahorro

    # --- Encapsulamiento ---
    @property
    def id_dispositivo_control(self) -> int:
        return self._id_dispositivo_control

    @property
    def id_usuario(self) -> int:
        return self._id_usuario

    @property
    def hora_de_conexion(self) -> str:
        return self._hora_de_conexion

    @property
    def dispositivos_activos(self) -> int:
        return self._dispositivos_activos

    @property
    def dispositivos_apagados(self) -> int:
        return self._dispositivos_apagados

    @property
    def dispositivos_en_ahorro(self) -> int:
        return self._dispositivos_en_ahorro

    def calcular_total_dispositivos(self) -> int:
        return self._dispositivos_activos + self._dispositivos_apagados + self._dispositivos_en_ahorro

    def __repr__(self) -> str:
        return (f"DispositivoControl(id={self._id_dispositivo_control}, usuario={self._id_usuario}, "
                f"activos={self._dispositivos_activos}, apagados={self._dispositivos_apagados}, "
                f"ahorro={self._dispositivos_en_ahorro})")
