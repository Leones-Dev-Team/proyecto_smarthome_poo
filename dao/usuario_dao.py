from typing import List, Optional
from dao.i_usuario_dao import IUsuarioDAO
from modelos.usuario import Usuario


class UsuarioDAO(IUsuarioDAO):
    """
    Implementación in-memory de IUsuarioDAO para simulación de persistencia.
    Usa una lista interna para almacenar usuarios.
    """

    def __init__(self):
        self._usuarios: List[Usuario] = []

    def crear(self, usuario: Usuario) -> bool:
        if any(u.id_usuario == usuario.id_usuario for u in self._usuarios):
            return False  # Ya existe
        self._usuarios.append(usuario)
        return True

    def leer(self, id_usuario: int) -> Optional[Usuario]:
        for u in self._usuarios:
            if u.id_usuario == id_usuario:
                return u
        return None

    def actualizar(self, usuario: Usuario) -> bool:
        for i, u in enumerate(self._usuarios):
            if u.id_usuario == usuario.id_usuario:
                self._usuarios[i] = usuario
                return True
        return False

    def eliminar(self, id_usuario: int) -> bool:
        for i, u in enumerate(self._usuarios):
            if u.id_usuario == id_usuario:
                del self._usuarios[i]
                return True
        return False

    def obtener_todos(self) -> List[Usuario]:
        return self._usuarios.copy()
