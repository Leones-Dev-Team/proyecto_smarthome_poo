from abc import ABC, abstractmethod
from typing import List
from dominio.automatizacion import Automatizacion
from dominio.dispositivo_hogar import DispositivoHogar


class IAutomatizacionDAO(ABC):
    @abstractmethod
    def crear(self, automatizacion: Automatizacion) -> int:
        pass

    @abstractmethod
    def leer(self, id_automatizacion: int) -> Automatizacion:
        pass

    @abstractmethod
    def actualizar(self, automatizacion: Automatizacion) -> bool:
        pass

    @abstractmethod
    def eliminar(self, id_automatizacion: int) -> bool:
        pass

    @abstractmethod
    def obtener_todos(self) -> List[Automatizacion]:
        pass

    @abstractmethod
    def agregar_dispositivo(self, id_automatizacion: int, id_dispositivo: int) -> bool:
        pass

    @abstractmethod
    def quitar_dispositivo(self, id_automatizacion: int, id_dispositivo: int) -> bool:
        pass

    @abstractmethod
    def obtener_dispositivos(self, id_automatizacion: int) -> List[DispositivoHogar]:
        pass
