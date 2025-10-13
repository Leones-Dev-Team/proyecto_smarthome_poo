import pytest
from unittest.mock import Mock
from dominio.hogar import Hogar
from dominio.dispositivo_hogar import DispositivoHogar
from dao.dispositivo_dao import DispositivoDAO


@pytest.fixture
def hogar_valido():
    return Hogar(id_hogar=1, ubicacion="Calle Principal 123", tipo_de_vivienda="Casa")


@pytest.fixture
def dispositivo_mock():
    dispositivo = Mock(spec=DispositivoHogar)
    dispositivo.id_hogar = 1
    dispositivo.id_dispositivo = "dev_001"
    dispositivo.nombre = "Luz Sala"
    dispositivo.tipo = "Iluminacion"
    return dispositivo


class TestHogarCreacion:
    def test_creacion_hogar_valido(self):
        hogar = Hogar(id_hogar=1, ubicacion="Avenida Libertad 456",
                      tipo_de_vivienda="Departamento")
        assert hogar.id_hogar == 1
        assert hogar.ubicacion == "Avenida Libertad 456"
        assert hogar.tipo_de_vivienda == "Departamento"

    def test_creacion_con_espacios_extra(self):
        hogar = Hogar(id_hogar=2, ubicacion="  Calle con espacios  ",
                      tipo_de_vivienda="  Casa grande  ")
        assert hogar.ubicacion == "Calle con espacios"
        assert hogar.tipo_de_vivienda == "Casa grande"

    def test_ubicacion_vacia_error(self):
        with pytest.raises(ValueError, match="La ubicacion no puede estar vacia"):
            Hogar(id_hogar=1, ubicacion="", tipo_de_vivienda="Casa")

    def test_ubicacion_solo_espacios_error(self):
        with pytest.raises(ValueError, match="La ubicacion no puede estar vacia"):
            Hogar(id_hogar=1, ubicacion="   ", tipo_de_vivienda="Casa")

    def test_tipo_vivienda_vacio_error(self):
        with pytest.raises(ValueError, match="El tipo de vivienda no puede estar vacio"):
            Hogar(id_hogar=1, ubicacion="Calle Principal 123", tipo_de_vivienda="")

    def test_tipo_vivienda_solo_espacios_error(self):
        with pytest.raises(ValueError, match="El tipo de vivienda no puede estar vacio"):
            Hogar(id_hogar=1, ubicacion="Calle Principal 123",
                  tipo_de_vivienda="   ")


class TestHogarPropiedades:
    def test_id_hogar_solo_lectura(self, hogar_valido):
        assert hogar_valido.id_hogar == 1
        with pytest.raises(AttributeError):
            hogar_valido.id_hogar = 999

    def test_ubicacion_getter(self, hogar_valido):
        assert hogar_valido.ubicacion == "Calle Principal 123"

    def test_ubicacion_setter_valido(self, hogar_valido):
        hogar_valido.ubicacion = "Nueva Ubicacion 789"
        assert hogar_valido.ubicacion == "Nueva Ubicacion 789"

    def test_ubicacion_setter_con_espacios(self, hogar_valido):
        hogar_valido.ubicacion = "  Ubicacion con espacios  "
        assert hogar_valido.ubicacion == "Ubicacion con espacios"

    def test_ubicacion_setter_vacia_error(self, hogar_valido):
        with pytest.raises(ValueError, match="La ubicacion no puede estar vacia"):
            hogar_valido.ubicacion = ""

    def test_ubicacion_setter_solo_espacios_error(self, hogar_valido):
        with pytest.raises(ValueError, match="La ubicacion no puede estar vacia"):
            hogar_valido.ubicacion = "   "

    def test_tipo_vivienda_getter(self, hogar_valido):
        assert hogar_valido.tipo_de_vivienda == "Casa"

    def test_tipo_vivienda_setter_valido(self, hogar_valido):
        hogar_valido.tipo_de_vivienda = "Departamento"
        assert hogar_valido.tipo_de_vivienda == "Departamento"

    def test_tipo_vivienda_setter_con_espacios(self, hogar_valido):
        hogar_valido.tipo_de_vivienda = "  Casa grande  "
        assert hogar_valido.tipo_de_vivienda == "Casa grande"

    def test_tipo_vivienda_setter_vacio_error(self, hogar_valido):
        with pytest.raises(ValueError, match="El tipo de vivienda no puede estar vacio"):
            hogar_valido.tipo_de_vivienda = ""

    def test_tipo_vivienda_setter_solo_espacios_error(self, hogar_valido):
        with pytest.raises(ValueError, match="El tipo de vivienda no puede estar vacio"):
            hogar_valido.tipo_de_vivienda = "   "


class TestHogarComposicionDispositivos:
    def test_listar_dispositivos_sin_dispositivos(self, hogar_valido):
        dao_mock = Mock(spec=DispositivoDAO)
        dao_mock.listar_por_hogar.return_value = []
        dispositivos = hogar_valido.listar_dispositivos_asociados(dao_mock)
        assert dispositivos == []
        dao_mock.listar_por_hogar.assert_called_once_with(1)

    def test_listar_dispositivos_con_dispositivos(self, hogar_valido, dispositivo_mock):
        dao_mock = Mock(spec=DispositivoDAO)
        dao_mock.listar_por_hogar.return_value = [dispositivo_mock]
        dispositivos = hogar_valido.listar_dispositivos_asociados(dao_mock)
        assert len(dispositivos) == 1
        assert dispositivos[0] == dispositivo_mock
        dao_mock.listar_por_hogar.assert_called_once_with(1)


class TestHogarRepresentaciones:
    def test_str_representation(self, hogar_valido):
        str_repr = str(hogar_valido)
        expected = "Hogar(id=1, ubicacion='Calle Principal 123', tipo='Casa')"
        assert str_repr == expected

    def test_repr_representation(self, hogar_valido):
        repr_str = repr(hogar_valido)
        expected = "Hogar(1, 'Calle Principal 123', 'Casa')"
        assert repr_str == expected


class TestHogarIntegracion:
    def test_escenario_completo_modificacion_propiedades(self):
        hogar = Hogar(id_hogar=10, ubicacion="Ubicacion Inicial",
                      tipo_de_vivienda="Casa Inicial")
        assert hogar.id_hogar == 10
        assert hogar.ubicacion == "Ubicacion Inicial"
        assert hogar.tipo_de_vivienda == "Casa Inicial"
        hogar.ubicacion = "Nueva Ubicacion"
        hogar.tipo_de_vivienda = "Departamento"
        assert hogar.ubicacion == "Nueva Ubicacion"
        assert hogar.tipo_de_vivienda == "Departamento"
        assert hogar.id_hogar == 10

    def test_validaciones_consistentes(self):
        hogar = Hogar(id_hogar=1, ubicacion="Ubicacion valida",
                      tipo_de_vivienda="Casa valida")
        with pytest.raises(ValueError, match="La ubicacion no puede estar vacia"):
            hogar.ubicacion = ""
        with pytest.raises(ValueError, match="La ubicacion no puede estar vacia"):
            hogar.ubicacion = "   "
        with pytest.raises(ValueError, match="El tipo de vivienda no puede estar vacio"):
            hogar.tipo_de_vivienda = ""
        with pytest.raises(ValueError, match="El tipo de vivienda no puede estar vacio"):
            hogar.tipo_de_vivienda = "   "
