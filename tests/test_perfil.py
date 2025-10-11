import pytest
from modelos.perfil import Perfil


@pytest.fixture
def perfil():
    return Perfil(nombre="Ana", mail="ana@mail.com", telefono="987654321")


def test_setters_validos(perfil):
    perfil.nombre = "Anna"
    perfil.mail = "anna@mail.com"
    perfil.telefono = "123456789"
    assert perfil.nombre == "Anna"
    assert perfil.mail == "anna@mail.com"
    assert perfil.telefono == "123456789"


def test_setters_invalidos(perfil):
    with pytest.raises(ValueError, match="El nombre debe ser una cadena no vacía"):
        perfil.nombre = ""
    with pytest.raises(ValueError, match="El mail debe ser una dirección válida"):
        perfil.mail = "correo-invalido"
    with pytest.raises(ValueError, match="El teléfono debe ser texto o None"):
        perfil.telefono = 12345  # no es str ni None


def test_registrar_actividad(perfil):
    perfil.registrar_actividad("Inicio de sesión")
    perfil.registrar_actividad("Configuró dispositivo")
    actividades = perfil.registro_actividad
    assert len(actividades) == 2
    assert any("Inicio de sesión" in act for act in actividades)
    assert any("Configuró dispositivo" in act for act in actividades)


def test_registro_es_inmutable(perfil):
    perfil.registrar_actividad("Prueba")
    log = perfil.registro_actividad
    with pytest.raises(AttributeError):
        log.append("No debería poder")  # tuple no tiene append
    assert len(perfil.registro_actividad) == 1  # intacto


def test_limpiar_registro(perfil):
    perfil.registrar_actividad("Algo")
    assert len(perfil.registro_actividad) == 1
    perfil.limpiar_registro()
    assert len(perfil.registro_actividad) == 0


def test_to_dict(perfil):
    perfil.registrar_actividad("Login")
    d = perfil.to_dict()
    assert d["nombre"] == "Ana"
    assert d["mail"] == "ana@mail.com"
    assert d["telefono"] == "987654321"
    assert isinstance(d["registro_actividad"], list)
    assert any("Login" in act for act in d["registro_actividad"])


def test_repr(perfil):
    r = repr(perfil)
    assert "Perfil" in r
    assert "Ana" in r
    assert "ana@mail.com" in r
