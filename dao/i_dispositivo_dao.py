import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modelos.dispositivo_hogar import DispositivoHogar
from abc import ABC, abstractmethod

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