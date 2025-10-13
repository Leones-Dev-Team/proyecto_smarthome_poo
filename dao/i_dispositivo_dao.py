from abc import ABC, abstractmethod
from typing import List, Optional
from modelos.dispositivo_hogar import DispositivoHogar


class IDispositivoDAO(ABC):
    """
    Interfaz DAO para operaciones CRUD sobre DispositivoHogar.
    Define los métodos abstractos para persistencia.
    """

    @abstractmethod
    def crear(self, dispositivo: DispositivoHogar) -> bool:
        """
        Crea un nuevo dispositivo en la base de datos.
        :param dispositivo: Instancia de DispositivoHogar a persistir.
        :return: True si se creó exitosamente, False en caso contrario.
        """
        pass

    @abstractmethod
    def leer(self, id_dispositivo: str) -> Optional[DispositivoHogar]:
        """
        Lee un dispositivo por su ID.
        :param id_dispositivo: ID único del dispositivo.
        :return: Instancia de DispositivoHogar si existe, None si no.
        """
        pass

    @abstractmethod
    def actualizar(self, dispositivo: DispositivoHogar) -> bool:
        """
        Actualiza un dispositivo existente.
        :param dispositivo: Instancia actualizada de DispositivoHogar.
        :return: True si se actualizó exitosamente, False en caso contrario.
        """
        pass

    @abstractmethod
    def eliminar(self, id_dispositivo: str) -> bool:
        """
        Elimina un dispositivo por su ID.
        :param id_dispositivo: ID único del dispositivo.
        :return: True si se eliminó exitosamente, False en caso contrario.
        """
        pass

    @abstractmethod
    def obtener_todos(self) -> List[DispositivoHogar]:
        """
        Obtiene todos los dispositivos.
        :return: Lista de instancias de DispositivoHogar.
        """
        pass
