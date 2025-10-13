from __future__ import annotations


class DispositivoHogar:
    """
    Representa un dispositivo inteligente del hogar.
    Posee atributos encapsulados y métodos públicos para su manejo.
    """

    def __init__(self, id_dispositivo: int, id_hogar: int, nombre: str, tipo: str,
                 marca: str | None, estado_dispositivo: str, consumo_energetico: float, es_esencial: bool):
        if not id_dispositivo or not nombre or not tipo or not estado_dispositivo or not consumo_energetico:
            raise ValueError("Los campos obligatorios no pueden estar vacios.")
        if estado_dispositivo not in ["encendido", "apagado"]:
            raise ValueError("El estado debe ser 'encendido' o 'apagado'.")
        self._id_dispositivo = id_dispositivo
        self._id_hogar = id_hogar
        self._nombre = nombre
        self._tipo = tipo
        self._marca = marca
        self._estado_dispositivo = estado_dispositivo
        self._consumo_energetico = consumo_energetico
        self._es_esencial = es_esencial

    # --- Encapsulamiento ---
    @property
    def id_dispositivo(self) -> int:
        return self._id_dispositivo

    @property
    def id_hogar(self) -> int:
        return self._id_hogar

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def tipo(self) -> str:
        return self._tipo

    @property
    def marca(self) -> str | None:
        return self._marca

    @property
    def estado_dispositivo(self) -> str:
        return self._estado_dispositivo

    @property
    def consumo_energetico(self) -> float:
        return self._consumo_energetico

    @property
    def es_esencial(self) -> bool:
        return self._es_esencial

    # --- Métodos de control ---
    def encender(self):
        self._estado_dispositivo = "encendido"

    def apagar(self):
        self._estado_dispositivo = "apagado"

    def toggle(self):
        self._estado_dispositivo = "apagado" if self._estado_dispositivo == "encendido" else "encendido"

    # --- Utilitario ---
    def __repr__(self):
        return f"<Dispositivo {self._nombre} ({self._tipo}) [Estado: {self._estado_dispositivo}, Consumo: {self._consumo_energetico}W]>"
