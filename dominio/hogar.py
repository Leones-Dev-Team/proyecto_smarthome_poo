from typing import List
from typing import List, TYPE_CHECKING
from dominio.dispositivo_hogar import DispositivoHogar

if TYPE_CHECKING:
    from dao.dispositivo_dao import DispositivoDAO


class Hogar:
    def __init__(self, id_hogar: int, ubicacion: str, tipo_de_vivienda: str):
        if not ubicacion or not ubicacion.strip():
            raise ValueError("La ubicacion no puede estar vacia")
        if not tipo_de_vivienda or not tipo_de_vivienda.strip():
            raise ValueError("El tipo de vivienda no puede estar vacio")
        self.__id_hogar = id_hogar
        self.__ubicacion = ubicacion.strip()
        self.__tipo_de_vivienda = tipo_de_vivienda.strip()

    @property
    def id_hogar(self) -> int:
        return self.__id_hogar

    @property
    def ubicacion(self) -> str:
        return self.__ubicacion

    @ubicacion.setter
    def ubicacion(self, nueva_ubicacion: str):
        if not nueva_ubicacion or not nueva_ubicacion.strip():
            raise ValueError("La ubicacion no puede estar vacia")
        self.__ubicacion = nueva_ubicacion.strip()

    @property
    def tipo_de_vivienda(self) -> str:
        return self.__tipo_de_vivienda

    @tipo_de_vivienda.setter
    def tipo_de_vivienda(self, nuevo_tipo: str):
        if not nuevo_tipo or not nuevo_tipo.strip():
            raise ValueError("El tipo de vivienda no puede estar vacio")
        self.__tipo_de_vivienda = nuevo_tipo.strip()

    def listar_dispositivos_asociados(self, dispositivo_dao: "DispositivoDAO") -> List[DispositivoHogar]:
        return dispositivo_dao.listar_por_hogar(self.__id_hogar)

    def __str__(self) -> str:
        return f"Hogar(id={self.__id_hogar}, ubicacion='{self.__ubicacion}', tipo='{self.__tipo_de_vivienda}')"

    def __repr__(self) -> str:
        return f"Hogar({self.__id_hogar}, '{self.__ubicacion}', '{self.__tipo_de_vivienda}')"
