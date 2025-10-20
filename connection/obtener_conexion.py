import mysql.connector
from mysql.connector import errorcode, Error  # Añadir errorcode al import
from dotenv import load_dotenv
from pathlib import Path
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
        env_path = Path(__file__).resolve().parent.parent / "db_connection.env"
        load_dotenv(dotenv_path=env_path)
        self.host = os.getenv('DB_HOST', 'localhost')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD', '')
        self.database = os.getenv('DB_DATABASE', 'smarthome')
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
        Establece y devuelve SIEMPRE una nueva conexión a la base de datos.
        """
        try:
            return mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                connection_timeout=10,
                autocommit=False
            )
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

    def close(self, conn):
        """Cierra la conexión recibida si está activa."""
        if conn and conn.is_connected():
            try:
                conn.close()
            except Error as e:
                print(f"Error al cerrar la conexión: {e}")

    @staticmethod
    def get_connection():
        """
        Método factory para obtener una conexión.
        Mantiene compatibilidad con el diseño original.
        """
        return obtener_conexion()
