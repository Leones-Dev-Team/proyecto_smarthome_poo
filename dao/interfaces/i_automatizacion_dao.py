from abc import ABC, abstractmethod
from typing import List
from modelos.automatizacion import Automatizacion
from modelos.dispositivo_hogar import DispositivoHogar

class IAutomatizacionDAO(ABC):
    """
    Interfaz DAO para operaciones CRUD sobre Automatizacion
    y su relación con dispositivos.
    """

    @abstractmethod
    def crear(self, automatizacion: Automatizacion) -> int:
        """Crea una nueva automatización y devuelve su ID."""
        pass

    @abstractmethod
    def leer(self, id_automatizacion: int) -> Automatizacion:
        """Lee una automatización por su ID."""
        pass

    @abstractmethod
    def actualizar(self, automatizacion: Automatizacion, id_automatizacion: int) -> bool:
        """Actualiza una automatización existente."""
        pass

    @abstractmethod
    def eliminar(self, id_automatizacion: int) -> bool:
        """Elimina una automatización por su ID."""
        pass

    @abstractmethod
    def obtener_todos(self) -> List[Automatizacion]:
        """Devuelve todas las automatizaciones almacenadas."""
        pass

    @abstractmethod
    def agregar_dispositivo(self, id_automatizacion: int, id_dispositivo: str) -> bool:
        """Asocia un dispositivo a una automatización."""
        pass

    @abstractmethod
    def quitar_dispositivo(self, id_automatizacion: int, id_dispositivo: str) -> bool:
        """Desasocia un dispositivo de una automatización."""
        pass

    @abstractmethod
    def obtener_dispositivos(self, id_automatizacion: int) -> List[DispositivoHogar]:
        """Devuelve los dispositivos asociados a una automatización."""
        pass
