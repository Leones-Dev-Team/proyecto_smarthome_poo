from abc import ABC, abstractmethod
from typing import List, Optional
from modelos.perfil import Perfil

class IPerfilDAO(ABC):
    """
    Interfaz DAO para operaciones CRUD sobre Perfil.
    """

    @abstractmethod
    def crear(self, perfil: Perfil) -> int:
        """
        Crea un nuevo perfil y devuelve su ID.
        :param perfil: Instancia de Perfil a persistir.
        :return: ID del perfil creado.
        """
        pass

    @abstractmethod
    def leer(self, id_perfil: int) -> Optional[Perfil]:
        """
        Lee un perfil por su ID.
        :param id_perfil: ID único del perfil.
        :return: Instancia de Perfil si existe, None si no.
        """
        pass

    @abstractmethod
    def actualizar(self, perfil: Perfil, id_perfil: int) -> bool:
        """
        Actualiza un perfil existente.
        :param perfil: Instancia actualizada de Perfil.
        :param id_perfil: ID del perfil a actualizar.
        :return: True si se actualizó exitosamente, False en caso contrario.
        """
        pass

    @abstractmethod
    def eliminar(self, id_perfil: int) -> bool:
        """
        Elimina un perfil por su ID.
        :param id_perfil: ID único del perfil.
        :return: True si se eliminó exitosamente, False en caso contrario.
        """
        pass

    @abstractmethod
    def obtener_todos(self) -> List[Perfil]:
        """
        Devuelve todos los perfiles almacenados.
        :return: Lista de instancias de Perfil.
        """
        pass
