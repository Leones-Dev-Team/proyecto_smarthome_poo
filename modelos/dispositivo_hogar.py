class DispositivoHogar:
    def __init__(self, id_dispositivo: str, estado_dispositivo: str, es_esencial: bool):
        self.id_dispositivo = id_dispositivo
        self.estado_dispositivo = estado_dispositivo  # "encendido" o "apagado"
        self._es_esencial = es_esencial

    def encender(self):
        self.estado_dispositivo = "encendido"

    def apagar(self):
        self.estado_dispositivo = "apagado"

    def es_esencial(self) -> bool:
        return self._es_esencial