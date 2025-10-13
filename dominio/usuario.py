from __future__ import annotations
from dominio.perfil import Perfil
from dominio.dispositivo_hogar import DispositivoHogar
from dao.dispositivo_dao import DispositivoDAO
from typing import List, Optional


class Usuario:
    """
    Clase que representa un usuario del sistema SmartHome.
    Aplica SRP: solo maneja credenciales, rol y relaciones con perfil y hogar.
    """

    def __init__(self, id_usuario: int, clave: str, rol: str, perfil: Perfil, id_hogar: int, edad: int):
        self._id_usuario = id_usuario
        self._clave = clave
        self._rol = rol if rol in ["admin", "estandar"] else "estandar"
        self._perfil = perfil
        self._id_hogar = id_hogar
        self._edad = edad

    # --- Encapsulamiento ---
    @property
    def id_usuario(self) -> int:
        return self._id_usuario

    @property
    def rol(self) -> str:
        return self._rol

    @rol.setter
    def rol(self, nuevo_rol: str):
        if nuevo_rol not in ["admin", "estandar"]:
            raise ValueError("Rol debe ser 'admin' o 'estandar'.")
        self._rol = nuevo_rol

    @property
    def perfil(self) -> Perfil:
        return self._perfil

    @property
    def id_hogar(self) -> int:
        return self._id_hogar

    @property
    def edad(self) -> int:
        return self._edad

    # --- Metodos funcionales ---
    def verificar_clave(self, clave: str) -> bool:
        return clave == self._clave

    def cambiar_clave(self, nueva_clave: str):
        if not nueva_clave:
            raise ValueError("La nueva clave no puede estar vacia.")
        self._clave = nueva_clave
        self._perfil.registrar_actividad("Cambio de clave de usuario")

    def mostrar_info(self) -> str:
        return (f"ID: {self._id_usuario}, Nombre: {self._perfil.nombre}, "
                f"Rol: {self._rol}, Edad: {self._edad}, "
                f"Correo: {self._perfil.mail}, Telefono: {self._perfil.telefono}, "
                f"Hogar ID: {self._id_hogar}")

    def __repr__(self) -> str:
        return f"Usuario(id={self._id_usuario}, rol={self._rol}, nombre={self._perfil.nombre})"
