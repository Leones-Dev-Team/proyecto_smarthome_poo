from typing import List, Optional
from dao.i_dispositivo_dao import IDispositivoDAO
from modelos.dispositivo_hogar import DispositivoHogar


class DispositivoDAO(IDispositivoDAO):
    """
    Implementación in-memory de IDispositivoDAO para simulación de persistencia.
    Usa una lista interna para almacenar dispositivos.
    """

    def __init__(self):
        self._dispositivos: List[DispositivoHogar] = []

    def crear(self, dispositivo: DispositivoHogar) -> bool:
        if any(d.id_dispositivo == dispositivo.id_dispositivo for d in self._dispositivos):
            return False  # Ya existe
        self._dispositivos.append(dispositivo)
        return True

    def leer(self, id_dispositivo: str) -> Optional[DispositivoHogar]:
        for d in self._dispositivos:
            if d.id_dispositivo == id_dispositivo:
                return d
        return None

    def actualizar(self, dispositivo: DispositivoHogar) -> bool:
        for i, d in enumerate(self._dispositivos):
            if d.id_dispositivo == dispositivo.id_dispositivo:
                self._dispositivos[i] = dispositivo
                return True
        return False

    def eliminar(self, id_dispositivo: str) -> bool:
        for i, d in enumerate(self._dispositivos):
            if d.id_dispositivo == id_dispositivo:
                del self._dispositivos[i]
                return True
        return False

    def obtener_todos(self) -> List[DispositivoHogar]:
        return self._dispositivos.copy()
