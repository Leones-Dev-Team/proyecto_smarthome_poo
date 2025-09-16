# usuario.py
class Usuario:
    def __init__(self, id_usuario: int, nombre: str, clave: str, rol: str,
                 tiempo_de_conexion: str, edad: int, mail: str, telefono: str,
                 registro_actividad: str, id_hogar: int = None):
        self._id_usuario = id_usuario
        self._nombre = nombre
        self._clave = clave
        self._rol = rol
        self._tiempo_de_conexion = tiempo_de_conexion
        self._edad = edad
        self._mail = mail
        self._telefono = telefono
        self._registro_actividad = registro_actividad
        self._id_hogar = id_hogar
        self.dispositivos_control = []
        self.dispositivos_hogar = []

    def get_id_usuario(self) -> int:
        """Devuelve el ID del usuario"""
        return self._id_usuario

    def verificar_clave(self, clave: str) -> bool:
        """Verifica si la clave ingresada coincide con la del usuario"""
        return self._clave == clave

    def cambiar_rol(self, nuevo_rol: str):
        """Cambia el rol del usuario"""
        self._rol = nuevo_rol

    def actualizar_datos(self, nombre: str = None, mail: str = None, telefono: str = None):
        """Actualiza los datos personales del usuario."""
        if nombre:
            self._nombre = nombre
        if mail:
            self._mail = mail
        if telefono:
            self._telefono = telefono

    def mostrar_info(self) -> str:
        """Devuelve un resumen de la información del usuario."""
        return (f"ID: {self._id_usuario}, Nombre: {self._nombre}, Rol: {self._rol}, "
                f"Edad: {self._edad}, Mail: {self._mail}, Teléfono: {self._telefono}")

    def cambiar_clave(self, nueva_clave: str):
        """Cambia la clave del usuario."""
        self._clave = nueva_clave

    def registrar_actividad(self, actividad: str):
        """Guarda solo la última actividad en el registro."""
        self._registro_actividad = actividad

    @property
    def rol(self) -> str:
        """Devuelve el rol del usuario"""
        return self._rol