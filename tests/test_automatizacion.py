import sys
import os
import pytest

# 🔧 Asegurar que Python vea el paquete raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modelos.automatizacion import Automatizacion
from modelos.dispositivo_hogar import DispositivoHogar


@pytest.fixture
def dispositivos_basicos():
    """Crea dispositivos de prueba (2 no esenciales, 1 esencial)."""
    d1 = DispositivoHogar(id_dispositivo="a1", nombre="Lámpara", tipo="luz", es_esencial=False)
    d2 = DispositivoHogar(id_dispositivo="a2", nombre="Ventilador", tipo="clima", es_esencial=False)
    d3 = DispositivoHogar(id_dispositivo="a3", nombre="Router", tipo="red", es_esencial=True)
    return d1, d2, d3


def test_activar_automatizacion_apaga_no_esenciales(dispositivos_basicos):
    """Debe apagar solo los dispositivos no esenciales encendidos."""
    d1, d2, d3 = dispositivos_basicos

    # Encendemos todos
    d1.encender()
    d2.encender()
    d3.encender()

    automatizacion = Automatizacion("Modo Ahorro", [d1, d2, d3])
    apagados = automatizacion.activar()

    assert apagados == 2  # solo d1 y d2 deben apagarse
    assert d1.estado_dispositivo is False
    assert d2.estado_dispositivo is False
    assert d3.estado_dispositivo is True  # esencial sigue encendido


def test_activar_automatizacion_sin_cambios():
    """No debe apagar nada si todos ya están apagados."""
    d1 = DispositivoHogar(id_dispositivo="a1", nombre="Lámpara", tipo="luz", es_esencial=False)
    d2 = DispositivoHogar(id_dispositivo="a2", nombre="Ventilador", tipo="clima", es_esencial=False)

    automatizacion = Automatizacion("Modo Ahorro", [d1, d2])
    apagados = automatizacion.activar()

    assert apagados == 0
    assert d1.estado_dispositivo is False
    assert d2.estado_dispositivo is False


def test_agregar_y_quitar_dispositivo():
    """Verifica agregar y quitar dispositivos de la automatización."""
    d1 = DispositivoHogar(id_dispositivo="x1", nombre="TV", tipo="video", es_esencial=False)
    d2 = DispositivoHogar(id_dispositivo="x2", nombre="Heladera", tipo="clima", es_esencial=True)

    automatizacion = Automatizacion("Prueba", [d1])
    assert len(automatizacion.dispositivos) == 1

    automatizacion.agregar_dispositivo(d2)
    assert len(automatizacion.dispositivos) == 2
    assert d2 in automatizacion.dispositivos

    automatizacion.quitar_dispositivo(d1)
    assert len(automatizacion.dispositivos) == 1
    assert d1 not in automatizacion.dispositivos
