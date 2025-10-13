import pytest
from dominio.dispositivo_hogar import DispositivoHogar
from dominio.automatizacion import Automatizacion


@pytest.fixture
def dispositivos_basicos():
    """Crea dispositivos de prueba (2 no esenciales, 1 esencial)."""
    d1 = DispositivoHogar(
        id_dispositivo=1,
        id_hogar=1,
        nombre="Lampara",
        tipo="luz",
        marca=None,
        estado_dispositivo="apagado",
        consumo_energetico=10.0,
        es_esencial=False
    )
    d2 = DispositivoHogar(
        id_dispositivo=2,
        id_hogar=1,
        nombre="Ventilador",
        tipo="clima",
        marca=None,
        estado_dispositivo="apagado",
        consumo_energetico=20.0,
        es_esencial=False
    )
    d3 = DispositivoHogar(
        id_dispositivo=3,
        id_hogar=1,
        nombre="Router",
        tipo="red",
        marca=None,
        estado_dispositivo="apagado",
        consumo_energetico=5.0,
        es_esencial=True
    )
    return d1, d2, d3


def test_activar_automatizacion_apaga_no_esenciales(dispositivos_basicos):
    d1, d2, d3 = dispositivos_basicos
    d1.encender()
    d2.encender()
    d3.encender()

    automatizacion = Automatizacion("Modo Ahorro", [d1, d2, d3])
    apagados = automatizacion.activar()

    assert apagados == 2
    assert d1.estado_dispositivo == "apagado"
    assert d2.estado_dispositivo == "apagado"
    assert d3.estado_dispositivo == "encendido"  # esencial sigue encendido


def test_activar_automatizacion_sin_cambios():
    d1 = DispositivoHogar(1, 1, "Lampara", "luz", None, "apagado", 10.0, False)
    d2 = DispositivoHogar(2, 1, "Ventilador", "clima",
                          None, "apagado", 20.0, False)

    automatizacion = Automatizacion("Modo Ahorro", [d1, d2])
    apagados = automatizacion.activar()

    assert apagados == 0
    assert d1.estado_dispositivo == "apagado"
    assert d2.estado_dispositivo == "apagado"


def test_agregar_y_quitar_dispositivo():
    d1 = DispositivoHogar(10, 1, "TV", "video", None, "apagado", 50.0, False)
    d2 = DispositivoHogar(11, 1, "Heladera", "clima",
                          "LG", "apagado", 150.0, True)

    automatizacion = Automatizacion("Prueba", [d1])
    assert len(automatizacion.dispositivos) == 1

    automatizacion.agregar_dispositivo(d2)
    assert len(automatizacion.dispositivos) == 2
    assert d2 in automatizacion.dispositivos

    automatizacion.quitar_dispositivo(d1)
    assert len(automatizacion.dispositivos) == 1
    assert d1 not in automatizacion.dispositivos
