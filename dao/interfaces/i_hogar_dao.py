from abc import ABC, abstractmethod
from typing import List, Optional
from dominio.hogar import Hogar


# Interfaz DAO que define las operaciones CRUD y utilitarias sobre la entidad Hogar
class IHogarDAO(ABC):
    @abstractmethod
    def crear(self, hogar: Hogar) -> bool:
        pass

    @abstractmethod
    def leer(self, id_hogar: int) -> Optional[Hogar]:
        pass

    @abstractmethod
    def actualizar(self, hogar: Hogar) -> bool:
        pass

    @abstractmethod
    def eliminar(self, id_hogar: int) -> bool:
        pass

    @abstractmethod
    def obtener_todos(self) -> List[Hogar]:
        pass

    @abstractmethod
    def existe(self, id_hogar: int) -> bool:
        pass

    @abstractmethod
    def obtener_siguiente_id(self) -> int:
        pass
