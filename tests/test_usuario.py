import pytest
from modelos.usuario import Usuario

@pytest.fixture
def usuario():
    return Usuario(
        id_usuario=1,
        nombre="Jonny",
        clave="1234",
        rol="admin",
        tiempo_de_conexion="2h",
        edad=30,
        mail="jonny@mail.com",
        telefono="123456789",
        registro_actividad="Inicio de sesión",
        id_hogar=101
    )

def test_mostrar_info(usuario):
    info = usuario.mostrar_info()
    assert "Jonny" in info
    assert "admin" in info

def test_id_hogar(usuario):
    assert usuario._id_hogar == 101

def test_verificar_clave(usuario):
    assert usuario.verificar_clave("1234")
    assert not usuario.verificar_clave("abcd")

def test_cambiar_rol(usuario):
    usuario.cambiar_rol("usuario")
    assert usuario.rol == "usuario"

def test_actualizar_datos(usuario):
    usuario.actualizar_datos(nombre="Jonathan", mail="jonathan@mail.com")
    info = usuario.mostrar_info()
    assert "Jonathan" in info
    assert "jonathan@mail.com" in info

def test_cambiar_clave(usuario):
    usuario.cambiar_clave("abcd")
    assert usuario.verificar_clave("abcd")

def test_registrar_actividad(usuario):
    usuario.registrar_actividad("Configuró dispositivo")
    assert usuario._registro_actividad == "Configuró dispositivo"

def test_dispositivos_control(usuario):
    usuario.dispositivos_control.append("Control 1")
    assert "Control 1" in usuario.dispositivos_control
    usuario.dispositivos_hogar.append("Dispositivo Hogar 1")
    assert "Dispositivo Hogar 1" in usuario.dispositivos_hogar