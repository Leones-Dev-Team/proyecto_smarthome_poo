from __future__ import annotations
from typing import List, Tuple
from datetime import datetime, timezone


class Perfil:
    """
    Representa el perfil personal de un usuario del sistema SmartHome.
    Encapsula datos personales y mantiene el registro de actividad.
    """

    def __init__(self, nombre: str, mail: str, telefono: str | None = None, id_perfil: int | None = None):
        self._validar_nombre(nombre)
        self._validar_mail(mail)
        self._id_perfil = id_perfil
        self._nombre = nombre
        self._mail = mail
        self._telefono = telefono
        self._registro_actividad: List[str] = []

    # ---- Validaciones internas ----
    @staticmethod
    def _validar_nombre(nombre: str):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre debe ser una cadena no vacia.")

    @staticmethod
    def _validar_mail(mail: str):
        if not isinstance(mail, str) or "@" not in mail or not mail.strip():
            raise ValueError("El mail debe ser una direccion valida.")

    # ---- Propiedades con encapsulamiento ----
    @property
    def id_perfil(self) -> int | None:
        return self._id_perfil

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self._validar_nombre(nuevo_nombre)
        self._nombre = nuevo_nombre

    @property
    def mail(self) -> str:
        return self._mail

    @mail.setter
    def mail(self, nuevo_mail: str):
        self._validar_mail(nuevo_mail)
        self._mail = nuevo_mail

    @property
    def telefono(self) -> str | None:
        return self._telefono

    @telefono.setter
    def telefono(self, nuevo_telefono: str | None):
        if nuevo_telefono and not isinstance(nuevo_telefono, str):
            raise ValueError("El telefono debe ser texto o None.")
        self._telefono = nuevo_telefono

    # ---- Registro de actividad ----
    def registrar_actividad(self, actividad: str) -> None:
        if not actividad or not isinstance(actividad, str):
            raise ValueError("Actividad invalida.")
        timestamp = datetime.now(timezone.utc).isoformat(
            timespec="seconds") + "Z"
        self._registro_actividad.append(f"{timestamp} - {actividad.strip()}")

    @property
    def registro_actividad(self) -> Tuple[str, ...]:
        return tuple(self._registro_actividad)

    def limpiar_registro(self):
        self._registro_actividad.clear()

    # ---- Utilitarios ----
    def to_dict(self) -> dict:
        return {
            "id_perfil": self._id_perfil,
            "nombre": self._nombre,
            "mail": self._mail,
            "telefono": self._telefono,
            "registro_actividad": list(self._registro_actividad),
        }

    def __repr__(self) -> str:
        return f"Perfil(id={self._id_perfil}, nombre={self._nombre!r}, mail={self._mail!r})"
