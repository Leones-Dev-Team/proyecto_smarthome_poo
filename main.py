from dao.dispositivo_dao import DispositivoDAO
from dao.usuario_dao import UsuarioDAO
from modelos.dispositivo_hogar import DispositivoHogar
from modelos.perfil import Perfil
from modelos.usuario import Usuario
import sys
import os

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'modelos')))
sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'dao')))


usuario_dao = UsuarioDAO()
dispositivo_dao = DispositivoDAO()


def registrar_usuario_estandar():
    # Registra un nuevo usuario estandar recolectando datos y guardandolos via DAO.
    try:
        id_usuario = int(input("Ingrese ID de usuario (numero unico): "))
        clave = input("Ingrese contrasena: ")
        nombre = input("Ingrese nombre: ")
        correo = input("Ingrese correo: ")
        telefono = input("Ingrese telefono (opcional): ") or None
        perfil = Perfil(nombre, correo, telefono)
        usuario = Usuario(id_usuario, clave, "user", perfil)
        if usuario_dao.crear(usuario):
            print(f"Usuario {nombre} registrado exitosamente como estandar.")
        else:
            print("Error al registrar usuario.")
    except ValueError as e:
        print(f"Error: {e}")


def login():
    # Maneja el inicio de sesion verificando credenciales via DAO.
    try:
        id_usuario = int(input("Ingrese ID de usuario: "))
        clave = input("Ingrese contrasena: ")
        usuario = usuario_dao.leer(id_usuario)
        if usuario and usuario.verificar_clave(clave):
            print(f"Bienvenido, {usuario.perfil.nombre} ({usuario.rol})")
            return usuario
        else:
            print("ID o contrasena incorrectos.")
            return None
    except ValueError:
        print("ID debe ser un numero.")
        return None


def menu_estandar(user):
    # Muestra menu para usuarios estandar para ver datos personales y dispositivos.
    while True:
        print("\nMenu Usuario Estandar:")
        print("1. Ver datos personales")
        print("2. Ver dispositivos")
        print("3. Salir")
        opcion = input("Seleccione opcion: ")
        if opcion == "1":
            print(user.mostrar_info())
            print(f"Nombre: {user.perfil.nombre}")
            print(f"Correo: {user.perfil.mail}")
            print(f"Telefono: {user.perfil.telefono}")
            print("Registro de actividad:")
            for actividad in user.perfil.registro_actividad:
                print(actividad)
        elif opcion == "2":
            dispositivos = user.dispositivos_hogar
            if dispositivos:
                print("Dispositivos asociados:")
                for dispositivo in dispositivos:
                    print(repr(dispositivo))
            else:
                print("No hay dispositivos asociados.")
        elif opcion == "3":
            break
        else:
            print("Opcion invalida.")


def menu_admin():
    # Muestra menu para administradores para gestionar dispositivos y roles de usuario.
    while True:
        print("\nMenu Admin:")
        print("1. Crear dispositivo")
        print("2. Leer dispositivo")
        print("3. Actualizar dispositivo")
        print("4. Eliminar dispositivo")
        print("5. Cambiar rol de usuario")
        print("6. Salir")
        opcion = input("Seleccione opcion: ")
        if opcion == "1":
            try:
                id_dispositivo = input("ID de dispositivo: ")
                nombre = input("Nombre: ")
                tipo = input("Tipo: ")
                es_esencial = input("Es esencial (y/n): ").lower() == 'y'
                dispositivo = DispositivoHogar(
                    id_dispositivo, nombre, tipo, es_esencial)
                if dispositivo_dao.crear(dispositivo):
                    print("Dispositivo creado.")
            except ValueError as e:
                print(f"Error: {e}")
        elif opcion == "2":
            id_dispositivo = input("ID de dispositivo: ")
            dispositivo = dispositivo_dao.leer(id_dispositivo)
            if dispositivo:
                print(repr(dispositivo))
            else:
                print("No encontrado.")
        elif opcion == "3":
            id_dispositivo = input("ID de dispositivo: ")
            dispositivo = dispositivo_dao.leer(id_dispositivo)
            if dispositivo:
                print("Actualizar estado: 1. Encender, 2. Apagar, 3. Cambiar")
                opt = input("Opcion: ")
                if opt == "1":
                    dispositivo.encender()
                elif opt == "2":
                    dispositivo.apagar()
                elif opt == "3":
                    dispositivo.toggle()
                if dispositivo_dao.actualizar(dispositivo):
                    print("Actualizado.")
            else:
                print("No encontrado.")
        elif opcion == "4":
            id_dispositivo = input("ID de dispositivo: ")
            if dispositivo_dao.eliminar(id_dispositivo):
                print("Eliminado.")
            else:
                print("No encontrado.")
        elif opcion == "5":
            try:
                id_usuario = int(input("ID de usuario a cambiar rol: "))
                usuario = usuario_dao.leer(id_usuario)
                if usuario:
                    nuevo_rol = input("Nuevo rol (admin/user): ")
                    usuario.rol = nuevo_rol
                    if usuario_dao.actualizar(usuario):
                        print("Rol cambiado.")
                else:
                    print("Usuario no encontrado.")
            except ValueError:
                print("Entrada invalida.")
        elif opcion == "6":
            break
        else:
            print("Opcion invalida.")


def main():
    # Bucle principal para manejar el flujo de la aplicacion.
    while True:
        print("\nSmartHome - Sistema de Gestion")
        print("1. Registrar nuevo usuario estandar")
        print("2. Iniciar sesion")
        print("3. Salir")
        opcion = input("Seleccione opcion: ")
        if opcion == "1":
            registrar_usuario_estandar()
        elif opcion == "2":
            usuario = login()
            if usuario:
                if usuario.rol == "user":
                    menu_estandar(usuario)
                elif usuario.rol == "admin":
                    menu_admin()
                else:
                    print("Rol desconocido.")
        elif opcion == "3":
            break
        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    main()
