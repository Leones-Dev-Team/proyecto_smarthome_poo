import sys
import os
from typing import List, Optional
from modelos.dispositivo_hogar import DispositivoHogar

# Agregar ruta del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class Automatizacion:
    """
    Representa una automatización de ahorro energético.
    Apaga dispositivos no esenciales. Agregación: dispositivos independientes.
    """

    def __init__(
        self,
        nombre: str,
        dispositivos: Optional[List[DispositivoHogar]] = None,
        id_automatizacion: Optional[int] = None
    ):
        if not nombre:
            raise ValueError("Nombre requerido.")
        self._id_automatizacion = id_automatizacion
        self._nombre = nombre
        self._dispositivos: List[DispositivoHogar] = dispositivos or []

    # Propiedades encapsuladas
    @property
    def id_automatizacion(self) -> Optional[int]:
        return self._id_automatizacion

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def dispositivos(self) -> tuple[DispositivoHogar, ...]:
        return tuple(self._dispositivos)

    # Métodos para agregación
    def agregar_dispositivo(self, dispositivo: DispositivoHogar):
        if dispositivo not in self._dispositivos:
            self._dispositivos.append(dispositivo)
            # Opcional: Persistir cambio vía DAO
            if self._id_automatizacion:
                from dao.automatizacion_dao import AutomatizacionDAO
                dao = AutomatizacionDAO()
                dao.agregar_dispositivo(self._id_automatizacion, dispositivo.id_dispositivo)

    def quitar_dispositivo(self, dispositivo: DispositivoHogar):
        if dispositivo in self._dispositivos:
            self._dispositivos.remove(dispositivo)
            # Opcional: Persistir cambio vía DAO
            if self._id_automatizacion:
                from dao.automatizacion_dao import AutomatizacionDAO
                dao = AutomatizacionDAO()
                dao.quitar_dispositivo(self._id_automatizacion, dispositivo.id_dispositivo)

    # Lógica principal
    def activar(self) -> int:
        apagados = 0
        for disp in self._dispositivos:
            if not disp.es_esencial() and disp.estado_dispositivo:
                disp.apagar()
                apagados += 1
                # Opcional: Actualizar BD si estado persiste
        return apagados

    # Persistencia (opcional, si se usa DAO)
    def guardar(self):
        from dao.automatizacion_dao import AutomatizacionDAO
        dao = AutomatizacionDAO()
        if self._id_automatizacion is None:
            self._id_automatizacion = dao.crear(self)
        else:
            dao.actualizar(self)

    @classmethod
    def cargar(cls, id_automatizacion: int) -> 'Automatizacion':
        from dao.automatizacion_dao import AutomatizacionDAO
        dao = AutomatizacionDAO()
        data = dao.leer(id_automatizacion)
        if data:
            # Cargar dispositivos desde BD
            return cls(
                data['nombre'],
                dao.obtener_dispositivos(id_automatizacion),
                id_automatizacion
            )
        raise ValueError("Automatización no encontrada.")

    def __repr__(self) -> str:
        return f"Automatizacion({self._nombre}, dispositivos={len(self._dispositivos)})"
