# test_dispositivo_control.py
import pytest
from modelos.dispositivo_control import DispositivoControl


def test_get_id_dispositivos_conectados():
    # Crea un control y verifica que el ID se obtenga correctamente
    control = DispositivoControl(
        id_dispositivos_conectados=1,
        id_usuarios_conectados=1,
        hora_de_conexion="10:00:00",
        dispositivos_activos=2,
        dispositivos_apagados=1,
        dispositivos_en_ahorro=0
    )
    assert control.get_id_dispositivos_conectados() == 1


def test_set_hora_conexion():
    # Prueba la actualización de la hora de conexión con formato válido
    control = DispositivoControl(
        id_dispositivos_conectados=1,
        id_usuarios_conectados=1,
        hora_de_conexion="10:00:00",
        dispositivos_activos=2,
        dispositivos_apagados=1,
        dispositivos_en_ahorro=0
    )
    control.set_hora_conexion("14:30:45")
    assert control._hora_de_conexion == "14:30:45"
    # Prueba con formato inválido
    with pytest.raises(ValueError):
        control.set_hora_conexion("invalido")


def test_calcular_total_dispositivos():
    # Verifica que el total de dispositivos se calcule correctamente
    control = DispositivoControl(
        id_dispositivos_conectados=1,
        id_usuarios_conectados=1,
        hora_de_conexion="10:00:00",
        dispositivos_activos=2,
        dispositivos_apagados=1,
        dispositivos_en_ahorro=0
    )
    assert control.calcular_total_dispositivos() == 3  # 2 + 1 + 0 = 3


def test_actualizar_dispositivos():
    # Actualiza los contadores y verifica que se reflejen correctamente
    control = DispositivoControl(
        id_dispositivos_conectados=1,
        id_usuarios_conectados=1,
        hora_de_conexion="10:00:00",
        dispositivos_activos=2,
        dispositivos_apagados=1,
        dispositivos_en_ahorro=0
    )
    control.set_dispositivos_activos(3)
    control.set_dispositivos_apagados(2)
    control.set_dispositivos_en_ahorro(1)
    assert control.dispositivos_activos == 3
    assert control.dispositivos_apagados == 2
    assert control.dispositivos_en_ahorro == 1
    # Prueba de validación
    with pytest.raises(ValueError):
        control.set_dispositivos_activos(-1)