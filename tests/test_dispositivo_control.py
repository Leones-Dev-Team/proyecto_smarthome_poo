# test_dispositivo_control.py
import pytest
from modelos.dispositivo_control import DispositivoControl


def test_get_id_dispositivo_control():
    # Crea un control y verifica que el ID se obtenga correctamente
    control = DispositivoControl(
        id_dispositivo_control=1,
        id_usuario_conectado=1,
        hora_de_conexion="10:00:00",
        dispositivos_activos=2,
        dispositivos_apagados=1,
        dispositivos_en_ahorro=0
    )
    assert control.get_id_dispositivo_control() == 1


def test_actualizar_dispositivos():
    # Actualiza los contadores y verifica que se reflejen correctamente
    control = DispositivoControl(
        id_dispositivo_control=1,
        id_usuario_conectado=1,
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
