from abc import ABC, abstractmethod
from typing import List, Optional
from modelos.usuario import Usuario

class IUsuarioDAO(ABC):
    """
    Interfaz DAO para operaciones CRUD sobre Usuario.
    """

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

    @abstractmethod
    def asociar_perfil(self, id_usuario: int, id_perfil: int) -> bool:
        """
        Asocia un perfil existente a un usuario.
        """
        pass

    @abstractmethod
    def desasociar_perfil(self, id_usuario: int) -> bool:
        """
        Elimina la asociación de perfil del usuario.
        """
        pass

    @abstractmethod
    def asignar_hogar(self, id_usuario: int, id_hogar: int) -> bool:
        """
        Asigna un hogar al usuario.
        """
        pass

    @abstractmethod
    def quitar_hogar(self, id_usuario: int) -> bool:
        """
        Elimina la asociación de hogar del usuario.
        """
        pass
