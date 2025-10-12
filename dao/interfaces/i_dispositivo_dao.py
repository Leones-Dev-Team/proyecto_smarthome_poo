from abc import ABC, abstractmethod
from typing import List, Optional
from modelos.dispositivo_hogar import DispositivoHogar

class IDispositivoDAO(ABC):
    """
    Interfaz DAO para operaciones CRUD sobre DispositivoHogar.
    """

    @abstractmethod
    def crear(self, dispositivo: DispositivoHogar) -> bool:
        pass

    @abstractmethod
    def leer(self, id_dispositivo: str) -> Optional[DispositivoHogar]:
        pass

    @abstractmethod
    def actualizar(self, dispositivo: DispositivoHogar) -> bool:
        pass

    @abstractmethod
    def eliminar(self, id_dispositivo: str) -> bool:
        pass

    @abstractmethod
    def obtener_todos(self) -> List[DispositivoHogar]:
        pass

    @abstractmethod
    def listar_por_automatizacion(self, id_automatizacion: int) -> List[DispositivoHogar]:
        """
        Devuelve los dispositivos asociados a una automatización.
        """
        pass

    @abstractmethod
    def actualizar_estado(self, id_dispositivo: str, nuevo_estado: bool) -> bool:
        """
        Actualiza el estado encendido/apagado de un dispositivo.
        """
        pass
