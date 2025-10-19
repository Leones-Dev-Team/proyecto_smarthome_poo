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
        self.__id_dispositivo = id_dispositivo
        self.__id_hogar = id_hogar
        self.__nombre = nombre
        self.__tipo = tipo
        self.__marca = marca
        self.__estado_dispositivo = estado_dispositivo
        self.__consumo_energetico = consumo_energetico
        self.__es_esencial = es_esencial

    # --- Encapsulamiento ---
    @property
    def id_dispositivo(self) -> int:
        return self.__id_dispositivo

    @property
    def id_hogar(self) -> int:
        return self.__id_hogar

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def tipo(self) -> str:
        return self.__tipo

    @property
    def marca(self) -> str | None:
        return self.__marca

    @property
    def estado_dispositivo(self) -> str:
        return self.__estado_dispositivo

    @property
    def consumo_energetico(self) -> float:
        return self.__consumo_energetico

    @property
    def es_esencial(self) -> bool:
        return self.__es_esencial

    # --- Métodos de control ---
    def encender(self):
        self.__estado_dispositivo = "encendido"

    def apagar(self):
        self.__estado_dispositivo = "apagado"

    def toggle(self):
        self.__estado_dispositivo = "apagado" if self.__estado_dispositivo == "encendido" else "encendido"

    # --- Utilitario ---
    def __repr__(self):
        return f"<Dispositivo {self.__nombre} ({self.__tipo}) [Estado: {self.__estado_dispositivo}, Consumo: {self.__consumo_energetico}W]>"
