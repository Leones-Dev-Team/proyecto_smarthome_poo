# modelos/hogar.py
from typing import List, Optional
from dao.dispositivo_dao import DispositivoDAO


class Hogar:
    """
    Clase que representa un hogar en el sistema SmartHome.
    Cumple con los principios (SRP, encapsulamiento) y se alinea 
    con la base de datos corregida.
    """
    
    def __init__(self, id_hogar: int, ubicacion: str, tipo_de_vivienda: str):
        """
        Inicializa un nuevo hogar con validaciones.
        
        Args:
            id_hogar: Identificador único del hogar
            ubicacion: Ubicación del hogar (no puede estar vacía)
            tipo_de_vivienda: Tipo de vivienda (no puede estar vacío)
            
        Raises:
            ValueError: Si ubicacion o tipo_de_vivienda están vacíos
        """
        if not ubicacion or not ubicacion.strip():
            raise ValueError("La ubicación no puede estar vacía")
        if not tipo_de_vivienda or not tipo_de_vivienda.strip():
            raise ValueError("El tipo de vivienda no puede estar vacío")
            
        self._id_hogar = id_hogar
        self._ubicacion = ubicacion.strip()
        self._tipo_de_vivienda = tipo_de_vivienda.strip()

    @property
    def id_hogar(self) -> int:
        """Getter para el ID del hogar (solo lectura)."""
        return self._id_hogar

    @property
    def ubicacion(self) -> str:
        """Getter para la ubicación del hogar."""
        return self._ubicacion

    @ubicacion.setter
    def ubicacion(self, nueva_ubicacion: str):
        """
        Setter para la ubicación del hogar con validación.
        
        Args:
            nueva_ubicacion: Nueva ubicación del hogar
            
        Raises:
            ValueError: Si la nueva ubicación está vacía
        """
        if not nueva_ubicacion or not nueva_ubicacion.strip():
            raise ValueError("La ubicación no puede estar vacía")
        self._ubicacion = nueva_ubicacion.strip()

    @property
    def tipo_de_vivienda(self) -> str:
        """Getter para el tipo de vivienda."""
        return self._tipo_de_vivienda

    @tipo_de_vivienda.setter
    def tipo_de_vivienda(self, nuevo_tipo: str):
        """
        Setter para el tipo de vivienda con validación.
        
        Args:
            nuevo_tipo: Nuevo tipo de vivienda
            
        Raises:
            ValueError: Si el nuevo tipo está vacío
        """
        if not nuevo_tipo or not nuevo_tipo.strip():
            raise ValueError("El tipo de vivienda no puede estar vacío")
        self._tipo_de_vivienda = nuevo_tipo.strip()

    def listar_dispositivos_asociados(self, dispositivo_dao: DispositivoDAO) -> List:
        """
        Lista todos los dispositivos asociados a este hogar.
        Implementa la composición con DispositivoHogar.
        
        Args:
            dispositivo_dao: Instancia del DAO para acceder a los dispositivos
            
        Returns:
            Lista de dispositivos asociados al hogar
        """
        todos_dispositivos = dispositivo_dao.obtener_todos()
        # Filtrar dispositivos que pertenecen a este hogar
        dispositivos_del_hogar = []
        for dispositivo in todos_dispositivos:
            # Verificar si el dispositivo tiene el atributo id_hogar y coincide
            if hasattr(dispositivo, 'id_hogar') and dispositivo.id_hogar == self._id_hogar:
                dispositivos_del_hogar.append(dispositivo)
        return dispositivos_del_hogar

    def __str__(self) -> str:
        """Representación en cadena del hogar."""
        return f"Hogar(id={self._id_hogar}, ubicacion='{self._ubicacion}', tipo='{self._tipo_de_vivienda}')"

    def __repr__(self) -> str:
        """Representación técnica del hogar."""
        return f"Hogar({self._id_hogar}, '{self._ubicacion}', '{self._tipo_de_vivienda}')"