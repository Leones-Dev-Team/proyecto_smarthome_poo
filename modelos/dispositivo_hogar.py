# modelos/dispositivo_hogar.py
from __future__ import annotations


class DispositivoHogar:
    """
    Representa un dispositivo inteligente del hogar.
    Posee atributos encapsulados y métodos públicos para su manejo.
    """

    def __init__(self, id_dispositivo, nombre, tipo, es_esencial=False):
        # Validaciones básicas
        if id_dispositivo == "":
            raise ValueError("El ID del dispositivo no puede estar vacío.")
        if nombre == "":
            raise ValueError("El nombre del dispositivo no puede estar vacío.")
        if tipo == "":
            raise ValueError("El tipo del dispositivo no puede estar vacío.")
        
        self._id_dispositivo = id_dispositivo
        self._nombre = nombre
        self._tipo = tipo
        self._es_esencial = es_esencial
        self._estado_dispositivo = False

    # --- Encapsulamiento ---
    @property
    def id_dispositivo(self):
        return self._id_dispositivo

    @property
    def nombre(self):
        return self._nombre

    @property
    def tipo(self):
        return self._tipo

    @property
    def estado_dispositivo(self):
        return self._estado_dispositivo

    # --- Métodos de control ---
    def encender(self):
        self._estado_dispositivo = True

    def apagar(self):
        self._estado_dispositivo = False

    def toggle(self):
        self._estado_dispositivo = not self._estado_dispositivo

    def es_esencial(self):
        return self._es_esencial
    
    def cambiar_nombre(self, nuevo_nombre):
        """Cambia el nombre del dispositivo."""
        if nuevo_nombre == "":
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = nuevo_nombre
    
    def obtener_estado_texto(self):
        """Retorna el estado como texto."""
        if self._estado_dispositivo:
            return "encendido"
        else:
            return "apagado"

    # --- Utilitario ---
    def __repr__(self):
        if self._estado_dispositivo:
            estado = "ON"
        else:
            estado = "OFF"
        
        resultado = "<Dispositivo " + self._nombre + " (" + self._tipo + ") [" + estado + "]"
        if self._es_esencial:
            resultado = resultado + " [ESENCIAL]"
        resultado = resultado + ">"
        return resultado
