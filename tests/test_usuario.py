import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modelos.usuario import Usuario

# Crear un usuario de prueba con id_hogar
usuario = Usuario(
    id_usuario=1,
    nombre="Jonny",
    clave="1234",
    rol="admin",
    tiempo_de_conexion="2h",
    edad=30,
    mail="jonny@mail.com",
    telefono="123456789",
    registro_actividad="Inicio de sesión",
    id_hogar=101
)

# Probar métodos básicos
print(usuario.mostrar_info())
print("ID Hogar:", usuario._id_hogar)
print("Clave correcta:", usuario.verificar_clave("1234"))
print("Clave incorrecta:", usuario.verificar_clave("abcd"))

usuario.cambiar_rol("usuario")
print("Nuevo rol:", usuario.rol)

usuario.actualizar_datos(nombre="Jonathan", mail="jonathan@mail.com")
print(usuario.mostrar_info())

usuario.cambiar_clave("abcd")
print("Clave actualizada:", usuario.verificar_clave("abcd"))

usuario.registrar_actividad("Configuró dispositivo")
print("Registro de actividad:", usuario._registro_actividad)

# Probar relación con dispositivos
usuario.dispositivos_control.append("Control 1")
usuario.dispositivos_hogar.append("Dispositivo Hogar 1")
print("Dispositivos de control:", usuario.dispositivos_control)
print("Dispositivos del hogar:", usuario.dispositivos_hogar)