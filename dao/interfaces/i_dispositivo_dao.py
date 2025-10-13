from abc import ABC, abstractmethod
from typing import List, Optional
from dominio.dispositivo_hogar import DispositivoHogar


class IDispositivoDAO(ABC):
    @abstractmethod
    def crear(self, dispositivo: DispositivoHogar) -> bool:
        pass

    @abstractmethod
    def leer(self, id_dispositivo: int) -> Optional[DispositivoHogar]:
        pass

    @abstractmethod
    def actualizar(self, dispositivo: DispositivoHogar) -> bool:
        pass

    @abstractmethod
    def eliminar(self, id_dispositivo: int) -> bool:
        pass

    @abstractmethod
    def obtener_todos(self) -> List[DispositivoHogar]:
        pass

    @abstractmethod
    def listar_por_hogar(self, id_hogar: int) -> List[DispositivoHogar]:
        pass
