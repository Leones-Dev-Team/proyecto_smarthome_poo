import pytest
from modelos.automatizacion import Automatizacion
from modelos.dispositivo_hogar import DispositivoHogar


def test_activar_automatizacion_apaga_no_esenciales():
    # 2 no esenciales encendidos, 1 esencial encendido
    d1 = DispositivoHogar(id_dispositivo="a1",
                          nombre="Lámpara", tipo="luz", es_esencial=False)
    d2 = DispositivoHogar(id_dispositivo="a2",
                          nombre="Ventilador", tipo="clima", es_esencial=False)
    d3 = DispositivoHogar(id_dispositivo="a3",
                          nombre="Router", tipo="red", es_esencial=True)

    # Encendemos todos
    d1.encender()
    d2.encender()
    d3.encender()

    automatizacion = Automatizacion("Modo Ahorro", [d1, d2, d3])

    apagados = automatizacion.activar()
    assert apagados == 2
    assert d1.estado_dispositivo is False
    assert d2.estado_dispositivo is False
    # El esencial sigue encendido
    assert d3.estado_dispositivo is True


def test_activar_automatizacion_sin_cambios():
    d1 = DispositivoHogar(id_dispositivo="a1",
                          nombre="Lámpara", tipo="luz", es_esencial=False)
    d2 = DispositivoHogar(id_dispositivo="a2",
                          nombre="Ventilador", tipo="clima", es_esencial=False)

    # Ambos ya están apagados por defecto
    automatizacion = Automatizacion("Modo Ahorro", [d1, d2])

    apagados = automatizacion.activar()
    assert apagados == 0
    assert d1.estado_dispositivo is False
    assert d2.estado_dispositivo is False
