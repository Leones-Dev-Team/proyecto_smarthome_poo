# modelos/usuario.py
from __future__ import annotations
from modelos.perfil import Perfil
from modelos.dispositivo_hogar import DispositivoHogar


class Usuario:
    """
    Clase que representa un usuario del sistema SmartHome.
    Aplica SRP: solo maneja credenciales y rol. 
    Delegación a Perfil para datos personales y actividades.
    """

    def __init__(self, id_usuario: int, clave: str, rol: str, perfil: Perfil | None = None):
        self._id_usuario = id_usuario
        self._clave = clave
        self._rol = rol
        self._perfil = perfil or Perfil("Sin nombre", "sin@mail.com")
        self._dispositivos_hogar: list[DispositivoHogar] = []

    # --- Encapsulamiento ---
    @property
    def id_usuario(self) -> int:
        return self._id_usuario

    @property
    def rol(self) -> str:
        return self._rol

    @rol.setter
    def rol(self, nuevo_rol: str):
        if not nuevo_rol:
            raise ValueError("El rol no puede estar vacío.")
        self._rol = nuevo_rol

    @property
    def perfil(self) -> Perfil:
        return self._perfil

    @property
    def dispositivos_hogar(self) -> tuple[DispositivoHogar, ...]:
        return tuple(self._dispositivos_hogar)

    # --- Métodos funcionales ---
    def verificar_clave(self, clave: str) -> bool:
        return clave == self._clave

    def cambiar_clave(self, nueva_clave: str):
        if not nueva_clave:
            raise ValueError("La nueva clave no puede estar vacía.")
        self._clave = nueva_clave
        self._perfil.registrar_actividad("Cambio de clave de usuario")

    def agregar_dispositivo(self, dispositivo: DispositivoHogar):
        if dispositivo not in self._dispositivos_hogar:
            self._dispositivos_hogar.append(dispositivo)
            self._perfil.registrar_actividad(
                f"Agregó dispositivo {dispositivo.nombre}")

    def quitar_dispositivo(self, dispositivo: DispositivoHogar):
        if dispositivo in self._dispositivos_hogar:
            self._dispositivos_hogar.remove(dispositivo)
            self._perfil.registrar_actividad(
                f"Quitó dispositivo {dispositivo.nombre}")

    def mostrar_info(self) -> str:
        return f"Usuario {self._id_usuario} ({self._rol}) - {self._perfil.nombre}"

    def __repr__(self):
        return f"Usuario(id={self._id_usuario}, rol={self._rol}, dispositivos={len(self._dispositivos_hogar)})"
