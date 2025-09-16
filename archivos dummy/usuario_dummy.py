class Usuario:
    def __init__(self, id_usuario: int, nombre: str, clave: str, rol: str,
                 tiempo_de_conexion: str, edad: int, mail: str, telefono: str,
                 registro_actividad: str, id_hogar: int = None):
        pass

    def get_id_usuario(self) -> int:
        """Devuelve el ID del usuario"""
        pass

    def verificar_clave(self, clave: str) -> bool:
        """Verifica si la clave ingresada coincide con la del usuario"""
        pass

    def cambiar_rol(self, nuevo_rol: str):
        """Cambia el rol del usuario"""
        pass

    def actualizar_datos(self, nombre: str = None, mail: str = None, telefono: str = None):
        """Actualiza los datos personales del usuario."""
        pass

    def mostrar_info(self) -> str:
        """Devuelve un resumen de la información del usuario."""
        pass

    def cambiar_clave(self, nueva_clave: str):
        """Cambia la clave del usuario."""
        pass

    def registrar_actividad(self, actividad: str):
        """Agrega una nueva actividad al registro."""
        pass

    @property
    def rol(self) -> str:
        """Devuelve el rol del usuario"""
        pass