from abc import ABC, abstractmethod
from typing import List, Optional
from dominio.perfil import Perfil


class IPerfilDAO(ABC):
    @abstractmethod
    def crear(self, perfil: Perfil) -> int:
        pass

    @abstractmethod
    def leer(self, id_perfil: int) -> Optional[Perfil]:
        pass

    @abstractmethod
    def actualizar(self, perfil: Perfil, id_perfil: int) -> bool:
        pass

    @abstractmethod
    def eliminar(self, id_perfil: int) -> bool:
        pass

    @abstractmethod
    def obtener_todos(self) -> List[Perfil]:
        pass
