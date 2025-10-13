from typing import List, Optional
from dominio.dispositivo_hogar import DispositivoHogar


class Automatizacion:
    """
    Representa una automatizacion de ahorro energetico.
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
            if self._id_automatizacion:
                from dao.automatizacion_dao import AutomatizacionDAO
                dao = AutomatizacionDAO()
                dao.agregar_dispositivo(
                    self._id_automatizacion, dispositivo.id_dispositivo)

    def quitar_dispositivo(self, dispositivo: DispositivoHogar):
        if dispositivo in self._dispositivos:
            self._dispositivos.remove(dispositivo)
            if self._id_automatizacion:
                from dao.automatizacion_dao import AutomatizacionDAO
                dao = AutomatizacionDAO()
                dao.quitar_dispositivo(
                    self._id_automatizacion, dispositivo.id_dispositivo)

    # Lógica principal
    def activar(self) -> int:
        apagados = 0
        for disp in self._dispositivos:
            if not disp.es_esencial and disp.estado_dispositivo == "encendido":
                disp.apagar()
                apagados += 1
                from dao.dispositivo_dao import DispositivoDAO
                dao = DispositivoDAO()
                dao.actualizar(disp)
        return apagados

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
        return cls(data.nombre, list(data.dispositivos), id_automatizacion)
