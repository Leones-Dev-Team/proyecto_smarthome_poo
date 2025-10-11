import pytest
from modelos.usuario import Usuario
from modelos.perfil import Perfil
from modelos.dispositivo_hogar import DispositivoHogar


@pytest.fixture
def usuario():
    perfil = Perfil(nombre="Jonny", mail="jonny@mail.com",
                    telefono="123456789")
    return Usuario(id_usuario=1, clave="1234", rol="admin", perfil=perfil)


def test_id_usuario(usuario):
    assert usuario.id_usuario == 1


def test_verificar_clave(usuario):
    assert usuario.verificar_clave("1234") is True
    assert usuario.verificar_clave("abcd") is False


def test_cambiar_rol_valido(usuario):
    usuario.rol = "usuario"
    assert usuario.rol == "usuario"


def test_cambiar_rol_invalido(usuario):
    with pytest.raises(ValueError, match="El rol no puede estar vacío"):
        usuario.rol = ""


def test_cambiar_clave_valida(usuario):
    usuario.cambiar_clave("abcd")
    assert usuario.verificar_clave("abcd") is True
    # además registra actividad en el perfil
    assert any(
        "Cambio de clave" in act for act in usuario.perfil.registro_actividad)


def test_cambiar_clave_invalida(usuario):
    with pytest.raises(ValueError, match="La nueva clave no puede estar vacía"):
        usuario.cambiar_clave("")


def test_mostrar_info(usuario):
    info = usuario.mostrar_info()
    assert "Usuario 1" in info
    assert "(admin)" in info
    assert "Jonny" in info


def test_agregar_y_quitar_dispositivo(usuario):
    dispositivo = DispositivoHogar(
        id_dispositivo="d1", nombre="Lámpara", tipo="luz")
    usuario.agregar_dispositivo(dispositivo)
    assert len(usuario.dispositivos_hogar) == 1
    assert dispositivo in usuario.dispositivos_hogar

    usuario.quitar_dispositivo(dispositivo)
    assert len(usuario.dispositivos_hogar) == 0
    # actividad registrada
    assert any(
        "Quitó dispositivo Lámpara" in act for act in usuario.perfil.registro_actividad)


def test_perfil_acceso(usuario):
    assert isinstance(usuario.perfil, Perfil)
    assert usuario.perfil.nombre == "Jonny"


# --- Nuevas pruebas básicas ---

def test_usuario_init_validaciones_basicas():
    """Prueba las validaciones básicas en el constructor."""
    with pytest.raises(ValueError):
        Usuario(id_usuario=0, clave="1234", rol="admin")
    
    with pytest.raises(ValueError):
        Usuario(id_usuario=1, clave="", rol="admin")
    
    with pytest.raises(ValueError):
        Usuario(id_usuario=1, clave="1234", rol="")


def test_cambiar_clave_validacion_basica(usuario):
    """Prueba la validación básica de cambio de clave."""
    with pytest.raises(ValueError):
        usuario.cambiar_clave("")


def test_buscar_dispositivo_por_id(usuario):
    """Prueba la búsqueda de dispositivos por ID."""
    dispositivo = DispositivoHogar("d1", "Lámpara", "luz")
    usuario.agregar_dispositivo(dispositivo)
    
    # Buscar dispositivo existente
    encontrado = usuario.buscar_dispositivo_por_id("d1")
    assert encontrado == dispositivo
    
    # Buscar dispositivo inexistente
    no_encontrado = usuario.buscar_dispositivo_por_id("inexistente")
    assert no_encontrado is None


def test_contar_dispositivos(usuario):
    """Prueba el conteo de dispositivos."""
    dispositivo1 = DispositivoHogar("d1", "Lámpara 1", "luz")
    dispositivo2 = DispositivoHogar("d2", "Lámpara 2", "luz")
    
    assert usuario.contar_dispositivos() == 0
    
    usuario.agregar_dispositivo(dispositivo1)
    assert usuario.contar_dispositivos() == 1
    
    usuario.agregar_dispositivo(dispositivo2)
    assert usuario.contar_dispositivos() == 2
    
    usuario.quitar_dispositivo(dispositivo1)
    assert usuario.contar_dispositivos() == 1
