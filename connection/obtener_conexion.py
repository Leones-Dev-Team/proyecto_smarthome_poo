import mysql.connector
from mysql.connector import errorcode, Error  # Añadir errorcode al import
from dotenv import load_dotenv
import os


def obtener_conexion():
    """
    Función de conveniencia para obtener una conexión a la base de datos.
    Utilizada por los DAOs para garantizar consistencia en el manejo de conexiones.
    """
    db = DatabaseConnection()
    return db.connect()


class DatabaseConnection:
    """
    Maneja conexiones a la base de datos MySQL para el sistema SmartHome.
    Provee un método para obtener una conexión reutilizable.
    Configuración cargada desde variables de entorno en un archivo .env.
    """

    def __init__(self):
        load_dotenv()
        self.host = os.getenv('DB_HOST', 'localhost')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD', '')
        self.database = os.getenv('DB_DATABASE', 'smarthome')
        self.connection = None
        self._validate_config()

    def _validate_config(self):
        """Valida las variables de entorno para la conexión a la base de datos."""
        if not self.user:
            raise ValueError("La variable de entorno DB_USER es requerida.")
        if not self.database:
            raise ValueError(
                "La variable de entorno DB_DATABASE es requerida.")
        if not self.host:
            raise ValueError("La variable de entorno DB_HOST es requerida.")

    def connect(self):
        """
        Establece y devuelve una conexión a la base de datos.
        Reutiliza la conexión existente si está activa.
        """
        if self.connection and self.connection.is_connected():
            return self.connection
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                connection_timeout=10
            )
            return self.connection
        except Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise ConnectionError(
                    "Error de autenticación: usuario o contraseña incorrectos.")
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                raise ConnectionError(
                    f"Base de datos '{self.database}' no encontrada.")
            else:
                raise ConnectionError(
                    f"Error conectando a la base de datos: {e}")

    def close(self):
        """Cierra la conexión si está activa."""
        if self.connection and self.connection.is_connected():
            try:
                self.connection.close()
                self.connection = None
            except Error as e:
                print(f"Error al cerrar la conexión: {e}")

    @staticmethod
    def get_connection():
        """
        Método factory para obtener una conexión.
        Mantiene compatibilidad con el diseño original.
        """
        return obtener_conexion()
