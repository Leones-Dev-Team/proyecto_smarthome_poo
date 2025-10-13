import pytest
from unittest.mock import Mock, MagicMock
from modelos.hogar import Hogar
from modelos.dispositivo_hogar import DispositivoHogar
from dao.dispositivo_dao import DispositivoDAO


@pytest.fixture
def hogar_valido():
    """Fixture que proporciona un hogar válido para las pruebas."""
    return Hogar(id_hogar=1, ubicacion="Calle Principal 123", tipo_de_vivienda="Casa")


@pytest.fixture
def dispositivo_mock():
    """Fixture que proporciona un dispositivo mock para las pruebas."""
    dispositivo = Mock(spec=DispositivoHogar)
    dispositivo.id_hogar = 1
    dispositivo.id_dispositivo = "dev_001"
    dispositivo.nombre = "Luz Sala"
    dispositivo.tipo = "Iluminación"
    return dispositivo


class TestHogarCreacion:
    """Tests para la creación e inicialización del hogar."""
    
    def test_creacion_hogar_valido(self):
        """Test que verifica la creación correcta de un hogar con datos válidos."""
        hogar = Hogar(id_hogar=1, ubicacion="Avenida Libertad 456", tipo_de_vivienda="Departamento")
        
        assert hogar.id_hogar == 1
        assert hogar.ubicacion == "Avenida Libertad 456"
        assert hogar.tipo_de_vivienda == "Departamento"
    
    def test_creacion_con_espacios_extra(self):
        """Test que verifica que se eliminan espacios extra al crear el hogar."""
        hogar = Hogar(id_hogar=2, ubicacion="  Calle con espacios  ", tipo_de_vivienda="  Casa grande  ")
        
        assert hogar.ubicacion == "Calle con espacios"
        assert hogar.tipo_de_vivienda == "Casa grande"
    
    def test_ubicacion_vacia_error(self):
        """Test que verifica que una ubicación vacía lanza ValueError."""
        with pytest.raises(ValueError, match="La ubicación no puede estar vacía"):
            Hogar(id_hogar=1, ubicacion="", tipo_de_vivienda="Casa")
    
    def test_ubicacion_solo_espacios_error(self):
        """Test que verifica que una ubicación con solo espacios lanza ValueError."""
        with pytest.raises(ValueError, match="La ubicación no puede estar vacía"):
            Hogar(id_hogar=1, ubicacion="   ", tipo_de_vivienda="Casa")
    
    def test_tipo_vivienda_vacio_error(self):
        """Test que verifica que un tipo de vivienda vacío lanza ValueError."""
        with pytest.raises(ValueError, match="El tipo de vivienda no puede estar vacío"):
            Hogar(id_hogar=1, ubicacion="Calle Principal 123", tipo_de_vivienda="")
    
    def test_tipo_vivienda_solo_espacios_error(self):
        """Test que verifica que un tipo de vivienda con solo espacios lanza ValueError."""
        with pytest.raises(ValueError, match="El tipo de vivienda no puede estar vacío"):
            Hogar(id_hogar=1, ubicacion="Calle Principal 123", tipo_de_vivienda="   ")


class TestHogarPropiedades:
    """Tests para las propiedades y su acceso controlado."""
    
    def test_id_hogar_solo_lectura(self, hogar_valido):
        """Test que verifica que el id_hogar es de solo lectura."""
        # id_hogar debe ser accesible
        assert hogar_valido.id_hogar == 1
        
        # Pero no debe tener setter (no debe poder asignarse)
        with pytest.raises(AttributeError):
            hogar_valido.id_hogar = 999
    
    def test_ubicacion_getter(self, hogar_valido):
        """Test que verifica el getter de ubicación."""
        assert hogar_valido.ubicacion == "Calle Principal 123"
    
    def test_ubicacion_setter_valido(self, hogar_valido):
        """Test que verifica el setter de ubicación con valor válido."""
        hogar_valido.ubicacion = "Nueva Ubicación 789"
        assert hogar_valido.ubicacion == "Nueva Ubicación 789"
    
    def test_ubicacion_setter_con_espacios(self, hogar_valido):
        """Test que verifica que el setter de ubicación elimina espacios extra."""
        hogar_valido.ubicacion = "  Ubicación con espacios  "
        assert hogar_valido.ubicacion == "Ubicación con espacios"
    
    def test_ubicacion_setter_vacia_error(self, hogar_valido):
        """Test que verifica que asignar ubicación vacía lanza ValueError."""
        with pytest.raises(ValueError, match="La ubicación no puede estar vacía"):
            hogar_valido.ubicacion = ""
    
    def test_ubicacion_setter_solo_espacios_error(self, hogar_valido):
        """Test que verifica que asignar ubicación con solo espacios lanza ValueError."""
        with pytest.raises(ValueError, match="La ubicación no puede estar vacía"):
            hogar_valido.ubicacion = "   "
    
    def test_tipo_vivienda_getter(self, hogar_valido):
        """Test que verifica el getter de tipo de vivienda."""
        assert hogar_valido.tipo_de_vivienda == "Casa"
    
    def test_tipo_vivienda_setter_valido(self, hogar_valido):
        """Test que verifica el setter de tipo de vivienda con valor válido."""
        hogar_valido.tipo_de_vivienda = "Departamento"
        assert hogar_valido.tipo_de_vivienda == "Departamento"
    
    def test_tipo_vivienda_setter_con_espacios(self, hogar_valido):
        """Test que verifica que el setter de tipo de vivienda elimina espacios extra."""
        hogar_valido.tipo_de_vivienda = "  Casa grande  "
        assert hogar_valido.tipo_de_vivienda == "Casa grande"
    
    def test_tipo_vivienda_setter_vacio_error(self, hogar_valido):
        """Test que verifica que asignar tipo de vivienda vacío lanza ValueError."""
        with pytest.raises(ValueError, match="El tipo de vivienda no puede estar vacío"):
            hogar_valido.tipo_de_vivienda = ""
    
    def test_tipo_vivienda_setter_solo_espacios_error(self, hogar_valido):
        """Test que verifica que asignar tipo de vivienda con solo espacios lanza ValueError."""
        with pytest.raises(ValueError, match="El tipo de vivienda no puede estar vacío"):
            hogar_valido.tipo_de_vivienda = "   "


class TestHogarComposicionDispositivos:
    """Tests para la composición con DispositivoHogar."""
    
    def test_listar_dispositivos_sin_dispositivos(self, hogar_valido):
        """Test que verifica el listado cuando no hay dispositivos."""
        dao_mock = Mock(spec=DispositivoDAO)
        dao_mock.obtener_todos.return_value = []
        
        dispositivos = hogar_valido.listar_dispositivos_asociados(dao_mock)
        
        assert dispositivos == []
        dao_mock.obtener_todos.assert_called_once()
    
    def test_listar_dispositivos_con_dispositivos_del_hogar(self, hogar_valido, dispositivo_mock):
        """Test que verifica el listado de dispositivos que pertenecen al hogar."""
        # Crear otro dispositivo que NO pertenece a este hogar
        otro_dispositivo = Mock(spec=DispositivoHogar)
        otro_dispositivo.id_hogar = 2  # Diferente ID de hogar
        otro_dispositivo.id_dispositivo = "dev_002"
        
        dao_mock = Mock(spec=DispositivoDAO)
        dao_mock.obtener_todos.return_value = [dispositivo_mock, otro_dispositivo]
        
        dispositivos = hogar_valido.listar_dispositivos_asociados(dao_mock)
        
        # Solo debe retornar el dispositivo que pertenece a este hogar (id_hogar=1)
        assert len(dispositivos) == 1
        assert dispositivos[0] == dispositivo_mock
        dao_mock.obtener_todos.assert_called_once()
    
    def test_listar_dispositivos_multiples_del_mismo_hogar(self, hogar_valido):
        """Test que verifica el listado cuando hay múltiples dispositivos del mismo hogar."""
        # Crear múltiples dispositivos del mismo hogar
        dispositivo1 = Mock(spec=DispositivoHogar)
        dispositivo1.id_hogar = 1
        dispositivo1.id_dispositivo = "dev_001"
        
        dispositivo2 = Mock(spec=DispositivoHogar)
        dispositivo2.id_hogar = 1
        dispositivo2.id_dispositivo = "dev_002"
        
        # Dispositivo de otro hogar
        dispositivo_otro_hogar = Mock(spec=DispositivoHogar)
        dispositivo_otro_hogar.id_hogar = 3
        dispositivo_otro_hogar.id_dispositivo = "dev_003"
        
        dao_mock = Mock(spec=DispositivoDAO)
        dao_mock.obtener_todos.return_value = [dispositivo1, dispositivo_otro_hogar, dispositivo2]
        
        dispositivos = hogar_valido.listar_dispositivos_asociados(dao_mock)
        
        # Debe retornar solo los 2 dispositivos del hogar 1
        assert len(dispositivos) == 2
        assert dispositivo1 in dispositivos
        assert dispositivo2 in dispositivos
        assert dispositivo_otro_hogar not in dispositivos
    
    def test_listar_dispositivos_sin_atributo_id_hogar(self, hogar_valido):
        """Test que verifica el comportamiento con dispositivos sin atributo id_hogar."""
        # Dispositivo sin atributo id_hogar
        dispositivo_sin_id_hogar = Mock(spec=DispositivoHogar)
        delattr(dispositivo_sin_id_hogar, 'id_hogar')  # Eliminar el atributo
        
        # Dispositivo con id_hogar correcto
        dispositivo_con_id = Mock(spec=DispositivoHogar)
        dispositivo_con_id.id_hogar = 1
        
        dao_mock = Mock(spec=DispositivoDAO)
        dao_mock.obtener_todos.return_value = [dispositivo_sin_id_hogar, dispositivo_con_id]
        
        dispositivos = hogar_valido.listar_dispositivos_asociados(dao_mock)
        
        # Solo debe retornar el dispositivo que tiene id_hogar y coincide
        assert len(dispositivos) == 1
        assert dispositivos[0] == dispositivo_con_id


class TestHogarRepresentaciones:
    """Tests para las representaciones string del hogar."""
    
    def test_str_representation(self, hogar_valido):
        """Test que verifica la representación string del hogar."""
        str_repr = str(hogar_valido)
        expected = "Hogar(id=1, ubicacion='Calle Principal 123', tipo='Casa')"
        assert str_repr == expected
    
    def test_repr_representation(self, hogar_valido):
        """Test que verifica la representación técnica del hogar."""
        repr_str = repr(hogar_valido)
        expected = "Hogar(1, 'Calle Principal 123', 'Casa')"
        assert repr_str == expected


class TestHogarIntegracion:
    """Tests de integración más complejos."""
    
    def test_escenario_completo_modificacion_propiedades(self):
        """Test que verifica un escenario completo de uso del hogar."""
        # Crear hogar
        hogar = Hogar(id_hogar=10, ubicacion="Ubicación Inicial", tipo_de_vivienda="Casa Inicial")
        
        # Verificar estado inicial
        assert hogar.id_hogar == 10
        assert hogar.ubicacion == "Ubicación Inicial"
        assert hogar.tipo_de_vivienda == "Casa Inicial"
        
        # Modificar propiedades
        hogar.ubicacion = "Nueva Ubicación"
        hogar.tipo_de_vivienda = "Departamento"
        
        # Verificar cambios
        assert hogar.ubicacion == "Nueva Ubicación"
        assert hogar.tipo_de_vivienda == "Departamento"
        assert hogar.id_hogar == 10  # ID no debe cambiar
    
    def test_validaciones_consistentes(self):
        """Test que verifica que las validaciones sean consistentes entre init y setters."""
        # Casos que deben fallar en init también deben fallar en setters
        hogar = Hogar(id_hogar=1, ubicacion="Ubicación válida", tipo_de_vivienda="Casa válida")
        
        # Ubicación
        with pytest.raises(ValueError, match="La ubicación no puede estar vacía"):
            hogar.ubicacion = ""
        with pytest.raises(ValueError, match="La ubicación no puede estar vacía"):
            hogar.ubicacion = "   "
        
        # Tipo de vivienda
        with pytest.raises(ValueError, match="El tipo de vivienda no puede estar vacío"):
            hogar.tipo_de_vivienda = ""
        with pytest.raises(ValueError, match="El tipo de vivienda no puede estar vacío"):
            hogar.tipo_de_vivienda = "   "