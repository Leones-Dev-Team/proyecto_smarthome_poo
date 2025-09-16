import pytest
from modelos.automatizacion import Automatizacion
from modelos.dispositivo_hogar import DispositivoHogar

def test_activar_automatizacion_apaga_no_esenciales():
    # Creamos dispositivos: 2 no esenciales encendidos, 1 esencial encendido
    d1 = DispositivoHogar("a1", "encendido", False)
    d2 = DispositivoHogar("a2", "encendido", False)
    d3 = DispositivoHogar("a3", "encendido", True)

    automatizacion = Automatizacion("Modo Ahorro", [d1, d2, d3])

    apagados = automatizacion.activar()

    # Debe apagar solo los no esenciales encendidos (2)
    assert apagados == 2
    assert d1.estado_dispositivo == "apagado"
    assert d2.estado_dispositivo == "apagado"
    assert d3.estado_dispositivo == "encendido"

def test_activar_automatizacion_sin_cambios():
    # Todos los dispositivos no esenciales ya están apagados
    d1 = DispositivoHogar("a1", "apagado", False)
    d2 = DispositivoHogar("a2", "apagado", False)

    automatizacion = Automatizacion("Modo Ahorro", [d1, d2])

    apagados = automatizacion.activar()

    # No debe apagar nada
    assert apagados == 0
    assert d1.estado_dispositivo == "apagado"
    assert d2.estado_dispositivo == "apagado"