import pytest
from modelos.usuario import Usuario


def test_get_id_usuario():
    # Crea un usuario y verifica que el ID se obtenga correctamente
    usuario = Usuario(
        id_usuario=1,
        nombre="lucas",
        clave="1234",
        rol="estandar",
        tiempo_de_conexion="00:10:00",
        edad=30,
        mail="lucas@example.com",
        telefono="123456789",
        registro_actividad="inicio de sesion"
    )
    assert usuario.get_id_usuario() == 1


def test_verificar_clave_correcta():
    # Verifica que la clave correcta devuelva True
    usuario = Usuario(
        id_usuario=1,
        nombre="lucas",
        clave="1234",
        rol="estandar",
        tiempo_de_conexion="00:10:00",
        edad=30,
        mail="lucas@example.com",
        telefono="123456789",
        registro_actividad="inicio de sesion"
    )
    assert usuario.verificar_clave("1234") is True


def test_cambiar_rol():
    # Cambia el rol y verifica que se actualice
    usuario = Usuario(
        id_usuario=1,
        nombre="lucas",
        clave="1234",
        rol="estandar",
        tiempo_de_conexion="00:10:00",
        edad=30,
        mail="lucas@example.com",
        telefono="123456789",
        registro_actividad="inicio de sesion"
    )
    usuario.cambiar_rol("administrador")
    assert usuario.rol == "administrador"
