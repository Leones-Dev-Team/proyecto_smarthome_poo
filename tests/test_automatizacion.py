# test_automatizacion.py
import pytest
from modelos.automatizacion import Automatizacion
from modelos.dispositivo_hogar import DispositivoHogar


def test_activar_automatizacion_apaga_no_esenciales():
    # Creamos dispositivos: 2 no esenciales encendidos, 1 esencial encendido
    d1 = DispositivoHogar("a1", 1, "living", "10:00:00",
                          "Luz 1", "luz", "Philips", "encendido", 10.5, False)
    d2 = DispositivoHogar("a2", 1, "cocina", "10:05:00",
                          "Luz 2", "luz", "Philips", "encendido", 8.0, False)
    d3 = DispositivoHogar("a3", 1, "baño", "10:10:00",
                          "Luz 3", "luz", "Philips", "encendido", 5.0, True)

    automatizacion = Automatizacion("Modo Ahorro", [d1, d2, d3])

    apagados = automatizacion.activar()

    # Debe apagar solo los no esenciales encendidos (2)
    assert apagados == 2
    assert d1.estado_dispositivo == "apagado"
    assert d2.estado_dispositivo == "apagado"
    assert d3.estado_dispositivo == "encendido"


def test_activar_automatizacion_sin_cambios():
    # Todos los dispositivos no esenciales ya estan apagados
    d1 = DispositivoHogar("a1", 1, "living", "10:00:00",
                          "Luz 1", "luz", "Philips", "apagado", 10.5, False)
    d2 = DispositivoHogar("a2", 1, "cocina", "10:05:00",
                          "Luz 2", "luz", "Philips", "apagado", 8.0, False)

    automatizacion = Automatizacion("Modo Ahorro", [d1, d2])

    apagados = automatizacion.activar()

    # No debe apagar nada
    assert apagados == 0
    assert d1.estado_dispositivo == "apagado"
    assert d2.estado_dispositivo == "apagado"
