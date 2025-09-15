# test_hogar.py
import pytest
from modelos.hogar import Hogar


def test_get_id_hogar():
    # Crea un hogar y verifica que el ID se obtenga correctamente
    hogar = Hogar(
        id_hogar=1,
        registro_actividad="actividad inicial",
        tiempo_de_conexion="01:23:45",
        ubicacion="Cordoba",
        tipo_de_vivienda="casa"
    )
    assert hogar.get_id_hogar() == 1


def test_set_registro_actividad():
    # Cambia el registro de actividad y comprueba que se actualice
    hogar = Hogar(
        id_hogar=1,
        registro_actividad="actividad inicial",
        tiempo_de_conexion="01:23:45",
        ubicacion="Cordoba",
        tipo_de_vivienda="casa"
    )
    hogar.set_registro_actividad("nueva actividad")
    assert hogar.registro_actividad == "nueva actividad"


def test_calcular_tiempo_formateado():
    # Verifica que el tiempo de conexion se devuelva en el formato esperado
    hogar = Hogar(
        id_hogar=1,
        registro_actividad="actividad inicial",
        tiempo_de_conexion="01:23:45",
        ubicacion="Cordoba",
        tipo_de_vivienda="casa"
    )
    assert hogar.calcular_tiempo_formateado() == "01:23:45"
