from abc import ABC, abstractmethod
from typing import List, Optional
from dominio.usuario import Usuario


class IUsuarioDAO(ABC):
    @abstractmethod
    def crear(self, usuario: Usuario) -> bool:
        pass

    @abstractmethod
    def leer(self, id_usuario: int) -> Optional[Usuario]:
        pass

    @abstractmethod
    def actualizar(self, usuario: Usuario) -> bool:
        pass

    @abstractmethod
    def eliminar(self, id_usuario: int) -> bool:
        pass

    @abstractmethod
    def obtener_todos(self) -> List[Usuario]:
        pass
