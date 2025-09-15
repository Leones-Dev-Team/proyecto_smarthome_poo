# test_dispositivo_hogar.py
import pytest
from modelos.dispositivo_hogar import DispositivoHogar


def test_get_id_dispositivo():
    # Crea un dispositivo y verifica que el ID se obtenga correctamente
    dispositivo = DispositivoHogar(
        id_dispositivo="a123",
        id_usuario_conectado=1,
        ubicacion="living",
        hora_de_conexion="10:00:00",
        nombre_dispositivo="Luz principal",
        tipo_dispositivo="luz",
        marca_dispositivo="Philips",
        estado_dispositivo="apagado",
        consumo_energetico=10.5,
        es_esencial=True
    )
    assert dispositivo.get_id_dispositivo() == "a123"


def test_encender_y_apagar():
    # Verifica que el dispositivo pueda encenderse y apagarse
    dispositivo = DispositivoHogar(
        id_dispositivo="a123",
        id_usuario_conectado=1,
        ubicacion="living",
        hora_de_conexion="10:00:00",
        nombre_dispositivo="Luz principal",
        tipo_dispositivo="luz",
        marca_dispositivo="Philips",
        estado_dispositivo="apagado",
        consumo_energetico=10.5,
        es_esencial=True
    )
    dispositivo.encender()
    assert dispositivo.estado_dispositivo == "encendido"
    dispositivo.apagar()
    assert dispositivo.estado_dispositivo == "apagado"


def test_es_esencial():
    # Verifica que el metodo es_esencial devuelva el valor correcto
    dispositivo = DispositivoHogar(
        id_dispositivo="a123",
        id_usuario_conectado=1,
        ubicacion="living",
        hora_de_conexion="10:00:00",
        nombre_dispositivo="Luz principal",
        tipo_dispositivo="luz",
        marca_dispositivo="Philips",
        estado_dispositivo="apagado",
        consumo_energetico=10.5,
        es_esencial=True
    )
    assert dispositivo.es_esencial() is True
