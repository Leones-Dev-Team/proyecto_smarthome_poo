# usuario.py
class Usuario:
    def __init__(self, id_usuario: int, nombre: str, clave: str, rol: str,
                 tiempo_de_conexion: str, edad: int, mail: str, telefono: str,
                 registro_actividad: str):
        self._id_usuario = id_usuario
        self._nombre = nombre
        self._clave = clave
        self._rol = rol
        self._tiempo_de_conexion = tiempo_de_conexion
        self._edad = edad
        self._mail = mail
        self._telefono = telefono
        self._registro_actividad = registro_actividad

    def get_id_usuario(self) -> int:
        """Devuelve el ID del usuario"""
        return self._id_usuario

    def verificar_clave(self, clave: str) -> bool:
        """Verifica si la clave ingresada coincide con la del usuario"""
        return self._clave == clave

    def cambiar_rol(self, nuevo_rol: str):
        """Cambia el rol del usuario"""
        self._rol = nuevo_rol

    @property
    def rol(self) -> str:
        """Devuelve el rol del usuario"""
        return self._rol
