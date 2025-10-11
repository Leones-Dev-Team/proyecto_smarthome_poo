# modelos/dispositivo_hogar.py
from __future__ import annotations


class DispositivoHogar:
    """
    Representa un dispositivo inteligente del hogar.
    Posee atributos encapsulados y métodos públicos para su manejo.
    """

    def __init__(self, id_dispositivo: str, nombre: str, tipo: str, es_esencial: bool = False):
        if not id_dispositivo or not nombre or not tipo:
            raise ValueError("Los campos id, nombre y tipo son obligatorios.")
        self._id_dispositivo = id_dispositivo
        self._nombre = nombre
        self._tipo = tipo
        self._es_esencial = es_esencial
        self._estado_dispositivo = False

    # --- Encapsulamiento ---
    @property
    def id_dispositivo(self) -> str:
        return self._id_dispositivo

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def tipo(self) -> str:
        return self._tipo

    @property
    def estado_dispositivo(self) -> bool:
        return self._estado_dispositivo

    # --- Métodos de control ---
    def encender(self):
        self._estado_dispositivo = True

    def apagar(self):
        self._estado_dispositivo = False

    def toggle(self):
        self._estado_dispositivo = not self._estado_dispositivo

    def es_esencial(self) -> bool:
        return self._es_esencial

    # --- Utilitario ---
    def __repr__(self):
        estado = "ON" if self._estado_dispositivo else "OFF"
        return f"<Dispositivo {self._nombre} ({self._tipo}) [{estado}]>"
