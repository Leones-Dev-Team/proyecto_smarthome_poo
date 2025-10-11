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
        pass

    def get_id_dispositivos_conectados(self) -> int:
        """Devuelve el ID de los dispositivos conectados."""
        pass

    def set_hora_conexion(self, nueva_hora: str) -> None:
        """Actualiza la hora de conexión con validación de formato 'HH:MM:SS'."""
        pass

    def calcular_total_dispositivos(self) -> int:
        """Calcula y devuelve el total de dispositivos (activos + apagados + en ahorro)."""
        pass

    def set_dispositivos_activos(self, cantidad: int):
        """Actualiza la cantidad de dispositivos activos con validación básica."""
        pass

    def set_dispositivos_apagados(self, cantidad: int):
        """Actualiza la cantidad de dispositivos apagados con validación básica."""
        pass

    def set_dispositivos_en_ahorro(self, cantidad: int):
        """Actualiza la cantidad de dispositivos en modo ahorro con validación básica."""
        pass

    @property
    def dispositivos_activos(self) -> int:
        """Devuelve la cantidad de dispositivos activos."""
        pass

    @property
    def dispositivos_apagados(self) -> int:
        """Devuelve la cantidad de dispositivos apagados."""
        pass

    @property
    def dispositivos_en_ahorro(self) -> int:
        """Devuelve la cantidad de dispositivos en modo ahorro."""
        pass