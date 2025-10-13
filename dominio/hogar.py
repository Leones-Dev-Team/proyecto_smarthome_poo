from typing import List
from dominio.dispositivo_hogar import DispositivoHogar
from dao.dispositivo_dao import DispositivoDAO


class Hogar:
    """
    Clase que representa un hogar en el sistema SmartHome.
    Cumple con los principios (SRP, encapsulamiento) y se alinea con la base de datos.
    """

    def __init__(self, id_hogar: int, ubicacion: str, tipo_de_vivienda: str):
        if not ubicacion or not ubicacion.strip():
            raise ValueError("La ubicacion no puede estar vacia")
        if not tipo_de_vivienda or not tipo_de_vivienda.strip():
            raise ValueError("El tipo de vivienda no puede estar vacio")
        self._id_hogar = id_hogar
        self._ubicacion = ubicacion.strip()
        self._tipo_de_vivienda = tipo_de_vivienda.strip()

    @property
    def id_hogar(self) -> int:
        return self._id_hogar

    @property
    def ubicacion(self) -> str:
        return self._ubicacion

    @ubicacion.setter
    def ubicacion(self, nueva_ubicacion: str):
        if not nueva_ubicacion or not nueva_ubicacion.strip():
            raise ValueError("La ubicacion no puede estar vacia")
        self._ubicacion = nueva_ubicacion.strip()

    @property
    def tipo_de_vivienda(self) -> str:
        return self._tipo_de_vivienda

    @tipo_de_vivienda.setter
    def tipo_de_vivienda(self, nuevo_tipo: str):
        if not nuevo_tipo or not nuevo_tipo.strip():
            raise ValueError("El tipo de vivienda no puede estar vacio")
        self._tipo_de_vivienda = nuevo_tipo.strip()

    def listar_dispositivos_asociados(self, dispositivo_dao: DispositivoDAO) -> List[DispositivoHogar]:
        return dispositivo_dao.listar_por_hogar(self._id_hogar)

    def __str__(self) -> str:
        return f"Hogar(id={self._id_hogar}, ubicacion='{self._ubicacion}', tipo='{self._tipo_de_vivienda}')"

    def __repr__(self) -> str:
        return f"Hogar({self._id_hogar}, '{self._ubicacion}', '{self._tipo_de_vivienda}')"
