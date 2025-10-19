from __future__ import annotations
from dominio.perfil import Perfil


class Usuario:
    """
    Clase que representa un usuario del sistema SmartHome.
    Aplica SRP: solo maneja credenciales, rol y relaciones con perfil y hogar.
    """

    def __init__(self, id_usuario: int, clave: str, rol: str, perfil: Perfil, id_hogar: int, edad: int):
        self.__id_usuario = id_usuario
        self.__clave = clave
        self.__rol = rol if rol in ["admin", "estandar"] else "estandar"
        self.__perfil = perfil
        self.__id_hogar = id_hogar
        self.__edad = edad

    # --- Encapsulamiento ---
    @property
    def id_usuario(self) -> int:
        return self.__id_usuario

    @property
    def rol(self) -> str:
        return self.__rol

    @rol.setter
    def rol(self, nuevo_rol: str):
        if nuevo_rol not in ["admin", "estandar"]:
            raise ValueError("Rol debe ser 'admin' o 'estandar'.")
        self.__rol = nuevo_rol

    @property
    def perfil(self) -> Perfil:
        return self.__perfil

    @property
    def id_hogar(self) -> int:
        return self.__id_hogar

    @property
    def edad(self) -> int:
        return self.__edad

    # --- Métodos funcionales ---
    def verificar_clave(self, clave: str) -> bool:
        return clave == self.__clave

    def cambiar_clave(self, nueva_clave: str):
        if not nueva_clave:
            raise ValueError("La nueva clave no puede estar vacia.")
        self.__clave = nueva_clave
        self.__perfil.registrar_actividad("Cambio de clave de usuario")

    def mostrar_info(self) -> str:
        return (f"ID: {self.__id_usuario}, Nombre: {self.__perfil.nombre}, "
                f"Rol: {self.__rol}, Edad: {self.__edad}, "
                f"Correo: {self.__perfil.mail}, Telefono: {self.__perfil.telefono}, "
                f"Hogar ID: {self.__id_hogar}")

    def __repr__(self) -> str:
        return f"Usuario(id={self.__id_usuario}, rol={self.__rol}, nombre={self.__perfil.nombre})"
