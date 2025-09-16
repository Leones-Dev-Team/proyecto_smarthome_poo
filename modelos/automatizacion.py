# automatizacion.py
class Automatizacion:
    def __init__(self, nombre: str, dispositivos: list):
        self._nombre = nombre
        self._dispositivos = dispositivos

    def activar(self) -> int:
        """
        Activa la automatización apagando todos los dispositivos
        no esenciales que estén encendidos.
        Devuelve la cantidad de dispositivos apagados.
        """
        dispositivos_apagados = 0
        for dispositivo in self._dispositivos:
            if not dispositivo.es_esencial() and dispositivo.estado_dispositivo == "encendido":
                dispositivo.apagar()
                dispositivos_apagados += 1
        return dispositivos_apagados