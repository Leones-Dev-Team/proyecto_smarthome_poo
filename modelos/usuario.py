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

    def __init__(self, id_usuario, clave, rol, perfil=None):
        # Validaciones básicas
        if id_usuario <= 0:
            raise ValueError("El ID de usuario debe ser un número positivo.")
        if clave == "":
            raise ValueError("La clave no puede estar vacía.")
        if rol == "":
            raise ValueError("El rol no puede estar vacío.")
        
        self._id_usuario = id_usuario
        self._clave = clave
        self._rol = rol
        if perfil is None:
            self._perfil = Perfil("Sin nombre", "sin@mail.com")
        else:
            self._perfil = perfil
        self._dispositivos_hogar = []

    # --- Encapsulamiento ---
    @property
    def id_usuario(self):
        return self._id_usuario

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, nuevo_rol):
        if nuevo_rol == "":
            raise ValueError("El rol no puede estar vacío.")
        self._rol = nuevo_rol

    @property
    def perfil(self):
        return self._perfil

    @property
    def dispositivos_hogar(self):
        # Devolver una copia de la lista para proteger el original
        return self._dispositivos_hogar.copy()

    # --- Métodos funcionales ---
    def verificar_clave(self, clave):
        return clave == self._clave

    def cambiar_clave(self, nueva_clave):
        if nueva_clave == "":
            raise ValueError("La nueva clave no puede estar vacía.")
        self._clave = nueva_clave
        self._perfil.registrar_actividad("Cambio de clave de usuario")

    def agregar_dispositivo(self, dispositivo):
        # Verificar que no esté ya en la lista
        if dispositivo not in self._dispositivos_hogar:
            self._dispositivos_hogar.append(dispositivo)
            self._perfil.registrar_actividad("Agregó dispositivo " + dispositivo.nombre)

    def quitar_dispositivo(self, dispositivo):
        # Verificar que esté en la lista antes de quitarlo
        if dispositivo in self._dispositivos_hogar:
            self._dispositivos_hogar.remove(dispositivo)
            self._perfil.registrar_actividad("Quitó dispositivo " + dispositivo.nombre)

    def buscar_dispositivo_por_id(self, id_dispositivo):
        """Busca un dispositivo por su ID."""
        for dispositivo in self._dispositivos_hogar:
            if dispositivo.id_dispositivo == id_dispositivo:
                return dispositivo
        return None
    
    def contar_dispositivos(self):
        """Cuenta cuántos dispositivos tiene el usuario."""
        return len(self._dispositivos_hogar)
    
    def mostrar_info(self):
        return "Usuario " + str(self._id_usuario) + " (" + self._rol + ") - " + self._perfil.nombre

    def __repr__(self):
        return "Usuario(id=" + str(self._id_usuario) + ", rol=" + self._rol + ", dispositivos=" + str(len(self._dispositivos_hogar)) + ")"
