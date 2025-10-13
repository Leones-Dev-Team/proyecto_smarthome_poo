from abc import ABC, abstractmethod
from typing import List, Optional
from modelos.usuario import Usuario


class IUsuarioDAO(ABC):
    """
    Interfaz DAO para operaciones CRUD sobre Usuario.
    Define los métodos abstractos para la persistencia y gestión de relaciones.
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
        Actualiza los datos de un usuario existente.
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
        Obtiene todos los usuarios almacenados.
        :return: Lista de instancias de Usuario.
        """
        pass

    @abstractmethod
    def asociar_perfil(self, id_usuario: int, id_perfil: int) -> bool:
        """
        Asocia un perfil existente a un usuario.
        :param id_usuario: ID del usuario.
        :param id_perfil: ID del perfil a asociar.
        :return: True si la asociación fue exitosa, False en caso contrario.
        """
        pass

    @abstractmethod
    def desasociar_perfil(self, id_usuario: int) -> bool:
        """
        Elimina la asociación de perfil del usuario.
        :param id_usuario: ID del usuario.
        :return: True si se desasoció correctamente, False en caso contrario.
        """
        pass

    @abstractmethod
    def asignar_hogar(self, id_usuario: int, id_hogar: int) -> bool:
        """
        Asigna un hogar existente a un usuario.
        :param id_usuario: ID del usuario.
        :param id_hogar: ID del hogar a asignar.
        :return: True si la asignación fue exitosa, False en caso contrario.
        """
        pass

    @abstractmethod
    def quitar_hogar(self, id_usuario: int) -> bool:
        """
        Elimina la asociación del hogar del usuario.
        :param id_usuario: ID del usuario.
        :return: True si se quitó correctamente, False en caso contrario.
        """
        pass
