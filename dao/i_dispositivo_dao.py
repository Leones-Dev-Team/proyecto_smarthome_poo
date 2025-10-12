from abc import ABC, abstractmethod
from typing import List, Optional
from modelos.usuario import Usuario


class IUsuarioDAO(ABC):
    """
    Interfaz DAO para operaciones CRUD sobre Usuario.
    Define los métodos abstractos para persistencia.
    """

    @abstractmethod
    def crear(self, usuario: Usuario) -> bool:
        """
        Crea un nuevo usuario en la base de datos.
        :param usuario: Instancia de Usuario a persistir.
        :return: True si se creó exitosamente, False en caso contrario.
        """
        pass

    @abstractmethod
    def leer(self, id_usuario: int) -> Optional[Usuario]:
        """
        Lee un usuario por su ID.
        :param id_usuario: ID único del usuario.
        :return: Instancia de Usuario si existe, None si no.
        """
        pass

    @abstractmethod
    def actualizar(self, usuario: Usuario) -> bool:
        """
        Actualiza un usuario existente.
        :param usuario: Instancia actualizada de Usuario.
        :return: True si se actualizó exitosamente, False en caso contrario.
        """
        pass

    @abstractmethod
    def eliminar(self, id_usuario: int) -> bool:
        """
        Elimina un usuario por su ID.
        :param id_usuario: ID único del usuario.
        :return: True si se eliminó exitosamente, False en caso contrario.
        """
        pass

    @abstractmethod
    def obtener_todos(self) -> List[Usuario]:
        """
        Obtiene todos los usuarios.
        :return: Lista de instancias de Usuario.
        """
        pass
