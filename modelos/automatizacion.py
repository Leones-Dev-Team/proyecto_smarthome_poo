import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modelos.dispositivo_hogar import DispositivoHogar
from typing import List


class Automatizacion:
    """
    Representa una automatización de ahorro energético.
    Apaga todos los dispositivos NO esenciales que estén encendidos.
    Relación de AGREGACIÓN: los dispositivos existen independientemente.
    """

    def __init__(self, nombre: str, dispositivos: List[DispositivoHogar]):
        if not nombre:
            raise ValueError(
                "El nombre de la automatización no puede estar vacío.")
        self._nombre = nombre
        self._dispositivos = dispositivos

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def dispositivos(self) -> tuple[DispositivoHogar, ...]:
        return tuple(self._dispositivos)

    def activar(self) -> int:
        """
        Activa la automatización apagando todos los dispositivos
        no esenciales que estén encendidos.
        Devuelve la cantidad de dispositivos apagados.
        """
        dispositivos_apagados = 0
        for dispositivo in self._dispositivos:
            if not dispositivo.es_esencial() and dispositivo.estado_dispositivo:
                dispositivo.apagar()
                dispositivos_apagados += 1
        return dispositivos_apagados

    def __repr__(self):
        return f"Automatizacion({self._nombre}, dispositivos={len(self._dispositivos)})"

#Prueba para verificar que funciona bien:

if __name__ == "__main__":
    # Ejemplo de uso
    from modelos.dispositivo_hogar import DispositivoHogar

    d1 = DispositivoHogar(id_dispositivo="a1", nombre="Lámpara", tipo="luz", es_esencial=False)
    d2 = DispositivoHogar(id_dispositivo="a2", nombre="Ventilador", tipo="clima", es_esencial=False)
    d1.encender()
    d2.encender()

    automatizacion = Automatizacion("Modo Ahorro", [d1, d2])
    apagados = automatizacion.activar()
    print(f"Dispositivos apagados: {apagados}")
