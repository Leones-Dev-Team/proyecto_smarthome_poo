import pytest
from modelos.dispositivo_hogar import DispositivoHogar


@pytest.fixture
def dispositivo():
    return DispositivoHogar(id_dispositivo="d1", nombre="Lámpara", tipo="luz", es_esencial=False)


def test_encender_apagar(dispositivo):
    dispositivo.encender()
    assert dispositivo.estado_dispositivo is True
    dispositivo.apagar()
    assert dispositivo.estado_dispositivo is False


def test_toggle(dispositivo):
    estado_inicial = dispositivo.estado_dispositivo
    dispositivo.toggle()
    assert dispositivo.estado_dispositivo is not estado_inicial
    dispositivo.toggle()
    assert dispositivo.estado_dispositivo == estado_inicial


def test_es_esencial(dispositivo):
    assert dispositivo.es_esencial() is False
    esencial = DispositivoHogar(
        id_dispositivo="e1", nombre="Router", tipo="red", es_esencial=True)
    assert esencial.es_esencial() is True


def test_id_acceso(dispositivo):
    assert dispositivo.id_dispositivo == "d1"  # Getter vía property


def test_repr(dispositivo):
    r = repr(dispositivo)
    assert "<Dispositivo" in r
    assert "Lámpara" in r
    assert "luz" in r


# --- Nuevas pruebas básicas ---

def test_dispositivo_init_validaciones_basicas():
    """Prueba las validaciones básicas en el constructor."""
    with pytest.raises(ValueError):
        DispositivoHogar("", "Nombre", "luz")
    
    with pytest.raises(ValueError):
        DispositivoHogar("d1", "", "luz")
    
    with pytest.raises(ValueError):
        DispositivoHogar("d1", "Nombre", "")


def test_cambiar_nombre():
    """Prueba el cambio de nombre del dispositivo."""
    dispositivo = DispositivoHogar("d1", "Nombre Original", "luz")
    
    nuevo_nombre = "Nombre Actualizado"
    dispositivo.cambiar_nombre(nuevo_nombre)
    assert dispositivo.nombre == nuevo_nombre
    
    # Validación
    with pytest.raises(ValueError):
        dispositivo.cambiar_nombre("")


def test_obtener_estado_texto():
    """Prueba el método de obtener estado como texto."""
    dispositivo = DispositivoHogar("d1", "Lámpara", "luz")
    
    # Estado inicial (apagado)
    assert dispositivo.obtener_estado_texto() == "apagado"
    
    # Encender dispositivo
    dispositivo.encender()
    assert dispositivo.obtener_estado_texto() == "encendido"
    
    # Apagar dispositivo
    dispositivo.apagar()
    assert dispositivo.obtener_estado_texto() == "apagado"


def test_repr_con_esencial():
    """Prueba la representación con indicador de esencial."""
    no_esencial = DispositivoHogar("d1", "Lámpara", "luz", es_esencial=False)
    esencial = DispositivoHogar("d2", "Router", "red", es_esencial=True)
    
    repr_no_esencial = repr(no_esencial)
    repr_esencial = repr(esencial)
    
    assert "[ESENCIAL]" not in repr_no_esencial
    assert "[ESENCIAL]" in repr_esencial
