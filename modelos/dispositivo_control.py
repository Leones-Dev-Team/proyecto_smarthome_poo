# dispositivo_control.py
class DispositivoControl:
    """
    Clase que representa el control de dispositivos en el sistema SmartHome.
    Gestiona contadores de estados y conexiones según el modelo entidad-relación.
    """
    def __init__(
        self,
        id_dispositivos_conectados: int,
        id_usuarios_conectados: int,
        hora_de_conexion: str,
        dispositivos_activos: int,
        dispositivos_apagados: int,
        dispositivos_en_ahorro: int
    ):
        """
        Inicializa los atributos privados de la clase.
        
        :param id_dispositivos_conectados: ID único del control (PK, INT).
        :param id_usuarios_conectados: ID del usuario conectado (FK, INT).
        :param hora_de_conexion: Hora de conexión en formato 'HH:MM:SS' (TIME, str).
        :param dispositivos_activos: Número de dispositivos activos (INT).
        :param dispositivos_apagados: Número de dispositivos apagados (INT).
        :param dispositivos_en_ahorro: Número de dispositivos en modo ahorro (INT).
        """
        self._id_dispositivos_conectados = id_dispositivos_conectados
        self._id_usuarios_conectados = id_usuarios_conectados
        self._hora_de_conexion = hora_de_conexion
        self._dispositivos_activos = dispositivos_activos
        self._dispositivos_apagados = dispositivos_apagados
        self._dispositivos_en_ahorro = dispositivos_en_ahorro

    def get_id_dispositivos_conectados(self) -> int:
        """Devuelve el ID de los dispositivos conectados."""
        return self._id_dispositivos_conectados

    def set_hora_conexion(self, nueva_hora: str) -> None:
        """Actualiza la hora de conexión con validación de formato 'HH:MM:SS'."""
        if not isinstance(nueva_hora, str) or len(nueva_hora) != 8 or nueva_hora.count(':') != 2:
            raise ValueError("La hora debe estar en formato 'HH:MM:SS'")
        self._hora_de_conexion = nueva_hora

    def calcular_total_dispositivos(self) -> int:
        """Calcula y devuelve el total de dispositivos (activos + apagados + en ahorro)."""
        return self._dispositivos_activos + self._dispositivos_apagados + self._dispositivos_en_ahorro

    def set_dispositivos_activos(self, cantidad: int):
        """Actualiza la cantidad de dispositivos activos con validación básica."""
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("La cantidad debe ser un entero no negativo")
        self._dispositivos_activos = cantidad

    def set_dispositivos_apagados(self, cantidad: int):
        """Actualiza la cantidad de dispositivos apagados con validación básica."""
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("La cantidad debe ser un entero no negativo")
        self._dispositivos_apagados = cantidad

    def set_dispositivos_en_ahorro(self, cantidad: int):
        """Actualiza la cantidad de dispositivos en modo ahorro con validación básica."""
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("La cantidad debe ser un entero no negativo")
        self._dispositivos_en_ahorro = cantidad

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