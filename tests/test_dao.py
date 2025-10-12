import pytest
from dao.dispositivo_dao import DispositivoDAO
from dao.usuario_dao import UsuarioDAO
from modelos.dispositivo_hogar import DispositivoHogar
from modelos.usuario import Usuario
from modelos.perfil import Perfil


@pytest.fixture
def dispositivo_dao():
    return DispositivoDAO()


@pytest.fixture
def usuario_dao():
    return UsuarioDAO()


def test_crud_dispositivo(dispositivo_dao):
    disp = DispositivoHogar("d1", "Lámpara", "luz")

    # Crear
    assert dispositivo_dao.crear(disp) is True
    assert len(dispositivo_dao.obtener_todos()) == 1

    # Leer
    read_disp = dispositivo_dao.leer("d1")
    assert read_disp is not None
    assert read_disp.nombre == "Lámpara"

    # Actualizar
    disp.encender()
    assert dispositivo_dao.actualizar(disp) is True
    updated = dispositivo_dao.leer("d1")
    assert updated.estado_dispositivo is True

    # Eliminar
    assert dispositivo_dao.eliminar("d1") is True
    assert len(dispositivo_dao.obtener_todos()) == 0


def test_crud_usuario(usuario_dao):
    perfil = Perfil("Test", "test@mail.com")
    user = Usuario(1, "pass", "user", perfil)

    # Crear
    assert usuario_dao.crear(user) is True
    assert len(usuario_dao.obtener_todos()) == 1

    # Leer
    read_user = usuario_dao.leer(1)
    assert read_user is not None
    assert read_user.rol == "user"

    # Actualizar
    user.rol = "admin"
    assert usuario_dao.actualizar(user) is True
    updated = usuario_dao.leer(1)
    assert updated.rol == "admin"

    # Eliminar
    assert usuario_dao.eliminar(1) is True
    assert len(usuario_dao.obtener_todos()) == 0
