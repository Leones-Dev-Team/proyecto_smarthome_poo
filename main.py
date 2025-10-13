from dao.dispositivo_dao import DispositivoDAO
from dao.usuario_dao import UsuarioDAO
from dao.perfil_dao import PerfilDAO
from dominio.dispositivo_hogar import DispositivoHogar
from dominio.perfil import Perfil
from dominio.usuario import Usuario
import sys
import os

# Configuracion de rutas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '../modelos')))
sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../dao')))

usuario_dao = UsuarioDAO()
dispositivo_dao = DispositivoDAO()
perfil_dao = PerfilDAO()


def registrar_usuario_estandar():
    try:
        id_usuario = int(input("Ingrese ID de usuario (numero unico): "))
        clave = input("Ingrese contrasena: ")
        nombre = input("Ingrese nombre: ")
        correo = input("Ingrese correo: ")
        telefono = input("Ingrese telefono (opcional): ") or None
        edad = int(input("Ingrese edad: "))
        id_hogar = int(input("Ingrese ID de hogar: "))
        perfil = Perfil(nombre, correo, telefono)
        id_perfil = perfil_dao.crear(perfil)
        usuario = Usuario(id_usuario, clave, "estandar",
                          perfil, id_hogar, edad)
        if usuario_dao.crear(usuario):
            print(f"Usuario {nombre} registrado exitosamente como estandar.")
        else:
            print("Error al registrar usuario.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


def login():
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
    while True:
        print("\nMenu Usuario Estandar:")
        print("1. Ver datos personales")
        print("2. Ver dispositivos")
        print("3. Salir")
        opcion = input("Seleccione opcion: ")
        if opcion == "1":
            print(user.mostrar_info())
        elif opcion == "2":
            dispositivos = dispositivo_dao.listar_por_hogar(user.id_hogar)
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
                id_dispositivo = int(input("ID de dispositivo: "))
                id_hogar = int(input("ID de hogar: "))
                nombre = input("Nombre: ")
                tipo = input("Tipo: ")
                marca = input("Marca (opcional): ") or None
                consumo = float(input("Consumo energetico (W): "))
                es_esencial = input("Es esencial (y/n): ").lower() == 'y'
                dispositivo = DispositivoHogar(
                    id_dispositivo, id_hogar, nombre, tipo, marca, "apagado", consumo, es_esencial)
                if dispositivo_dao.crear(dispositivo):
                    print("Dispositivo creado.")
                else:
                    print("Error al crear dispositivo.")
            except ValueError as e:
                print(f"Error: {e}")
        elif opcion == "2":
            try:
                id_dispositivo = int(input("ID de dispositivo: "))
                dispositivo = dispositivo_dao.leer(id_dispositivo)
                if dispositivo:
                    print(repr(dispositivo))
                else:
                    print("No encontrado.")
            except ValueError:
                print("ID debe ser un numero.")
        elif opcion == "3":
            try:
                id_dispositivo = int(input("ID de dispositivo: "))
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
                        print("Error al actualizar.")
                else:
                    print("No encontrado.")
            except ValueError:
                print("ID debe ser un numero.")
        elif opcion == "4":
            try:
                id_dispositivo = int(input("ID de dispositivo: "))
                if dispositivo_dao.eliminar(id_dispositivo):
                    print("Eliminado.")
                else:
                    print("No encontrado.")
            except ValueError:
                print("ID debe ser un numero.")
        elif opcion == "5":
            try:
                id_usuario = int(input("ID de usuario a cambiar rol: "))
                usuario = usuario_dao.leer(id_usuario)
                if usuario:
                    nuevo_rol = input("Nuevo rol (admin/estandar): ")
                    if nuevo_rol in ["admin", "estandar"]:
                        usuario.rol = nuevo_rol
                        if usuario_dao.actualizar(usuario):
                            print("Rol cambiado.")
                        else:
                            print("Error al cambiar rol.")
                    else:
                        print("Rol invalido.")
                else:
                    print("Usuario no encontrado.")
            except ValueError:
                print("Entrada invalida.")
        elif opcion == "6":
            break
        else:
            print("Opcion invalida.")


def main():
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
                if usuario.rol == "estandar":
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
