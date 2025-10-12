from abc import ABC, abstractmethod
from modelos.dispositivo_hogar import DispositivoHogar

class IDispositivoDAO(ABC):
    @abstractmethod
    def guardar(self, dispositivo: DispositivoHogar):
        pass

    @abstractmethod
    def obtener(self, id_dispositivo: str) -> DispositivoHogar:
        pass

    @abstractmethod
    def eliminar(self, id_dispositivo: str):
        pass

    @abstractmethod
    def listar(self) -> list[DispositivoHogar]:
        pass