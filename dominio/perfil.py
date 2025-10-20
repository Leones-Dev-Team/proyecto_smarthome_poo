from __future__ import annotations
from typing import List, Tuple
from datetime import datetime, timezone


class Perfil:
    """
    Representa el perfil personal de un usuario del sistema SmartHome.
    Encapsula datos personales y mantiene el registro de actividad.
    """

    def __init__(self, nombre: str, mail: str, telefono: str | None = None, id_perfil: int = 0):
        self._validar_nombre(nombre)
        self._validar_mail(mail)
        self.__id_perfil: int = id_perfil  # siempre int, 0 si aún no está en DB
        self.__nombre = nombre
        self.__mail = mail
        self.__telefono = telefono
        self.__registro_actividad: List[str] = []

    # ---- Validaciones internas ----
    @staticmethod
    def _validar_nombre(nombre: str):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre debe ser una cadena no vacía.")

    @staticmethod
    def _validar_mail(mail: str):
        if not isinstance(mail, str) or "@" not in mail or not mail.strip():
            raise ValueError("El mail debe ser una dirección válida.")

    # ---- Propiedades con encapsulamiento ----
    @property
    def id_perfil(self) -> int:
        return self.__id_perfil

    @id_perfil.setter
    def id_perfil(self, nuevo_id: int) -> None:
        if not isinstance(nuevo_id, int) or nuevo_id < 0:
            raise ValueError("El id_perfil debe ser un entero no negativo.")
        self.__id_perfil = nuevo_id

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self._validar_nombre(nuevo_nombre)
        self.__nombre = nuevo_nombre

    @property
    def mail(self) -> str:
        return self.__mail

    @mail.setter
    def mail(self, nuevo_mail: str):
        self._validar_mail(nuevo_mail)
        self.__mail = nuevo_mail

    @property
    def telefono(self) -> str | None:
        return self.__telefono

    @telefono.setter
    def telefono(self, nuevo_telefono: str | None):
        if nuevo_telefono and not isinstance(nuevo_telefono, str):
            raise ValueError("El teléfono debe ser texto o None.")
        self.__telefono = nuevo_telefono

    # ---- Registro de actividad ----
    def registrar_actividad(self, actividad: str) -> None:
        if not actividad or not isinstance(actividad, str):
            raise ValueError("Actividad inválida.")
        timestamp = datetime.now(timezone.utc).isoformat(
            timespec="seconds") + "Z"
        self.__registro_actividad.append(f"{timestamp} - {actividad.strip()}")

    @property
    def registro_actividad(self) -> Tuple[str, ...]:
        return tuple(self.__registro_actividad)

    def limpiar_registro(self):
        self.__registro_actividad.clear()

    def cargar_registro(self, registro: str) -> None:
        if registro:
            self.__registro_actividad = registro.split(", ")
        else:
            self.__registro_actividad = []

    # ---- Utilitarios ----
    def to_dict(self) -> dict:
        return {
            "id_perfil": self.__id_perfil,
            "nombre": self.__nombre,
            "mail": self.__mail,
            "telefono": self.__telefono,
            "registro_actividad": list(self.__registro_actividad),
        }

    def __repr__(self) -> str:
        return f"Perfil(id={self.__id_perfil}, nombre={self.__nombre!r}, mail={self.__mail!r})"
