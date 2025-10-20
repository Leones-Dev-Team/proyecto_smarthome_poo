import pytest
from dominio.usuario import Usuario
from dominio.perfil import Perfil


@pytest.fixture
def usuario():
    perfil = Perfil(nombre="Jonny", mail="jonny@mail.com",
                    telefono="123456789")
    return Usuario(id_usuario=1, clave="1234", rol="admin", perfil=perfil, id_hogar=10, edad=25)


def test_id_usuario(usuario):
    assert usuario.id_usuario == 1


def test_verificar_clave(usuario):
    assert usuario.verificar_clave("1234") is True
    assert usuario.verificar_clave("abcd") is False


def test_cambiar_rol_valido(usuario):
    usuario.rol = "estandar"
    assert usuario.rol == "estandar"


def test_cambiar_rol_invalido(usuario):
    with pytest.raises(ValueError, match="Rol debe ser 'admin' o 'estandar'."):
        usuario.rol = "otro"


def test_propiedad_clave(usuario):
    assert usuario.clave == "1234"
    usuario.cambiar_clave("nueva")
    assert usuario.clave == "nueva"


def test_cambiar_clave_valida(usuario):
    usuario.cambiar_clave("abcd")
    assert usuario.verificar_clave("abcd") is True
    assert any(
        "Cambio de clave" in act for act in usuario.perfil.registro_actividad)


def test_cambiar_clave_invalida(usuario):
    with pytest.raises(ValueError, match="La nueva clave no puede estar vacía."):
        usuario.cambiar_clave("")


def test_mostrar_info(usuario):
    info = usuario.mostrar_info()
    assert "ID: 1" in info
    assert "Rol: admin" in info
    assert "Jonny" in info


def test_perfil_acceso(usuario):
    assert isinstance(usuario.perfil, Perfil)
    assert usuario.perfil.nombre == "Jonny"
