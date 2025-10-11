import pytest
from modelos.dispositivo_hogar import DispositivoHogar


@pytest.fixture
def dispositivo():
    return DispositivoHogar(id_dispositivo="d1", nombre="Lámpara", tipo="luz", es_esencial=False)


def test_encender_apagar(dispositivo):
    dispositivo.encender()
    assert dispositivo.estado_dispositivo is True
    dispositivo.apagar()
    assert dispositivo.estado_dispositivo is False


def test_toggle(dispositivo):
    estado_inicial = dispositivo.estado_dispositivo
    dispositivo.toggle()
    assert dispositivo.estado_dispositivo is not estado_inicial
    dispositivo.toggle()
    assert dispositivo.estado_dispositivo == estado_inicial


def test_es_esencial(dispositivo):
    assert dispositivo.es_esencial() is False
    esencial = DispositivoHogar(
        id_dispositivo="e1", nombre="Router", tipo="red", es_esencial=True)
    assert esencial.es_esencial() is True


def test_id_acceso(dispositivo):
    assert dispositivo.id_dispositivo == "d1"


def test_repr(dispositivo):
    r = repr(dispositivo)
    assert "<Dispositivo" in r
    assert "Lámpara" in r
    assert "luz" in r
