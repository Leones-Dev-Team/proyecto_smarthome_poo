import pytest
from dominio.dispositivo_hogar import DispositivoHogar


@pytest.fixture
def dispositivo():
    return DispositivoHogar(
        id_dispositivo=1,
        id_hogar=1,
        nombre="Lampara",
        tipo="luz",
        marca=None,
        estado_dispositivo="apagado",
        consumo_energetico=10.5,
        es_esencial=False
    )


def test_encender_apagar(dispositivo):
    dispositivo.encender()
    assert dispositivo.estado_dispositivo == "encendido"
    dispositivo.apagar()
    assert dispositivo.estado_dispositivo == "apagado"


def test_toggle(dispositivo):
    estado_inicial = dispositivo.estado_dispositivo
    dispositivo.toggle()
    assert dispositivo.estado_dispositivo != estado_inicial
    dispositivo.toggle()
    assert dispositivo.estado_dispositivo == estado_inicial


def test_es_esencial(dispositivo):
    assert dispositivo.es_esencial is False
    esencial = DispositivoHogar(
        id_dispositivo=2,
        id_hogar=2,
        nombre="Router",
        tipo="red",
        marca="Cisco",
        estado_dispositivo="apagado",
        consumo_energetico=5.0,
        es_esencial=True
    )
    assert esencial.es_esencial is True


def test_id_acceso(dispositivo):
    assert dispositivo.id_dispositivo == 1


def test_repr(dispositivo):
    r = repr(dispositivo)
    assert "<Dispositivo" in r
    assert "Lampara" in r
    assert "luz" in r
    assert "apagado" in r
