from dao.dispositivo_dao import DispositivoDAO
from dao.usuario_dao import UsuarioDAO
from dao.perfil_dao import PerfilDAO
from dao.hogar_dao import HogarDAO
from dominio.dispositivo_hogar import DispositivoHogar
from dominio.perfil import Perfil
from dominio.usuario import Usuario
import sys
import os
import re

# Configuración de rutas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '../modelos')))
sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../dao')))

usuario_dao = UsuarioDAO()
dispositivo_dao = DispositivoDAO()
perfil_dao = PerfilDAO()
hogar_dao = HogarDAO()


def validar_email(correo: str) -> bool:
    """Valida que el correo tenga un formato válido."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, correo))


def mostrar_lista_hogares():
    """Muestra lista de hogares disponibles y retorna la lista."""
    hogares = hogar_dao.obtener_todos()
    if not hogares:
        print("No hay hogares disponibles.")
        return None
    print("Hogares disponibles:")
    for idx, hogar in enumerate(hogares, 1):
        print(
            f"{idx}. ID: {hogar.id_hogar}, Ubicación: {hogar.ubicacion}, Tipo: {hogar.tipo_de_vivienda}")
    return hogares


def seleccionar_hogar(hogares):
    """Permite seleccionar un hogar de la lista por número."""
    try:
        opcion = int(input("Seleccione el número del hogar: "))
        if 1 <= opcion <= len(hogares):
            return hogares[opcion - 1].id_hogar
        else:
            print("Opción inválida.")
            return None
    except ValueError:
        print("Entrada inválida. Debe ser un número.")
        return None


def mostrar_lista_dispositivos(id_hogar):
    """Muestra lista de dispositivos para un hogar y retorna la lista."""
    dispositivos = dispositivo_dao.listar_por_hogar(id_hogar)
    if not dispositivos:
        print("No hay dispositivos disponibles.")
        return None
    print("Dispositivos disponibles:")
    for idx, disp in enumerate(dispositivos, 1):
        print(f"{idx}. {repr(disp)}")
    return dispositivos


def seleccionar_dispositivo(dispositivos):
    """Permite seleccionar un dispositivo por número."""
    try:
        opcion = int(input("Seleccione el número del dispositivo: "))
        if 1 <= opcion <= len(dispositivos):
            return dispositivos[opcion - 1]
        else:
            print("Opción inválida.")
            return None
    except ValueError:
        print("Entrada inválida. Debe ser un número.")
        return None


def registrar_usuario_estandar():
    """Registra un usuario estándar con ID auto-generado y selección de hogar."""
    try:
        # Generar ID de usuario automáticamente
        id_usuario = usuario_dao.obtener_siguiente_id()  # Asumido: método en UsuarioDAO

        clave = input("Ingrese contraseña: ")
        if not clave:
            print("La contraseña no puede estar vacía.")
            return

        nombre = input("Ingrese nombre: ")
        if not nombre:
            print("El nombre no puede estar vacío.")
            return

        correo = input("Ingrese correo: ").strip().lower()
        if not validar_email(correo):
            print("Correo inválido.")
            return

        telefono = input("Ingrese telefono (opcional): ") or None
        try:
            edad = int(input("Ingrese edad: "))
            if edad <= 0:
                print("La edad debe ser un número positivo.")
                return
        except ValueError:
            print("La edad debe ser un número entero.")
            return

        # Mostrar y seleccionar hogar
        hogares = mostrar_lista_hogares()
        if not hogares:
            return
        id_hogar = seleccionar_hogar(hogares)
        if not id_hogar or not hogar_dao.existe(id_hogar):
            print("Hogar no encontrado.")
            return

        # Construir el perfil, sin insertarlo aquí
        perfil = Perfil(nombre, correo, telefono)

        # Crear usuario; UsuarioDAO se encargará de crear el perfil y asociarlo
        usuario = Usuario(id_usuario, clave, "estandar",
                          perfil, id_hogar, edad)
        if usuario_dao.crear(usuario):
            print(
                f"Usuario {nombre} registrado exitosamente como estándar con ID {id_usuario}.")
        else:
            print("Error al registrar usuario.")
    except ValueError as e:
        print(f"Error de entrada: {e}")
    except Exception as e:
        if "1364" in str(e):  # Error de MySQL para campo sin valor por defecto
            print("Error: Problema con el perfil (posiblemente sin valor por defecto en la base de datos). Contacte al administrador.")
        else:
            print(f"Error inesperado: {e}")


def login():
    """Inicia sesión usando email en lugar de ID."""
    try:
        correo = input("Ingrese correo: ")
        if not validar_email(correo):
            print("Correo inválido.")
            return None
        clave = input("Ingrese contraseña: ")
        # Asumido: nuevo método en UsuarioDAO
        usuario = usuario_dao.leer_por_email(correo)
        if usuario and usuario.verificar_clave(clave):
            print(f"Bienvenido, {usuario.perfil.nombre} ({usuario.rol})")
            return usuario
        else:
            print("Correo o contraseña incorrectos.")
            return None
    except ValueError:
        print("Entrada inválida.")
        return None


def menu_estandar(user):
    """Menú para usuarios estándar."""
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
    """Menú para administradores con selección de dispositivos/hogares."""
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
                # Generar ID de dispositivo automáticamente
                # Asumido: método en DispositivoDAO
                id_dispositivo = dispositivo_dao.obtener_siguiente_id()

                # Seleccionar hogar
                hogares = mostrar_lista_hogares()
                if not hogares:
                    continue
                id_hogar = seleccionar_hogar(hogares)
                if not id_hogar:
                    continue

                nombre = input("Nombre: ")
                if not nombre:
                    print("El nombre no puede estar vacío.")
                    continue
                tipo = input("Tipo: ")
                if not tipo:
                    print("El tipo no puede estar vacío.")
                    continue
                marca = input("Marca (opcional): ") or None
                try:
                    consumo = float(input("Consumo energetico (W): "))
                    if consumo < 0:
                        print("El consumo no puede ser negativo.")
                        continue
                except ValueError:
                    print("El consumo debe ser un número.")
                    continue
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
                # Seleccionar hogar primero
                hogares = mostrar_lista_hogares()
                if not hogares:
                    continue
                id_hogar = seleccionar_hogar(hogares)
                if not id_hogar:
                    continue
                dispositivos = mostrar_lista_dispositivos(id_hogar)
                if dispositivos:
                    disp = seleccionar_dispositivo(dispositivos)
                    if disp:
                        print(repr(disp))
                    else:
                        print("No seleccionado.")
            except ValueError:
                print("Entrada inválida.")
        elif opcion == "3":
            try:
                # Seleccionar hogar y dispositivo
                hogares = mostrar_lista_hogares()
                if not hogares:
                    continue
                id_hogar = seleccionar_hogar(hogares)
                if not id_hogar:
                    continue
                dispositivos = mostrar_lista_dispositivos(id_hogar)
                if dispositivos:
                    disp = seleccionar_dispositivo(dispositivos)
                    if disp:
                        print("Actualizar estado: 1. Encender, 2. Apagar, 3. Cambiar")
                        opt = input("Opcion: ")
                        if opt == "1":
                            disp.encender()
                        elif opt == "2":
                            disp.apagar()
                        elif opt == "3":
                            disp.toggle()
                        else:
                            print("Opción inválida.")
                            continue
                        if dispositivo_dao.actualizar(disp):
                            print("Actualizado.")
                        else:
                            print("Error al actualizar.")
            except ValueError:
                print("Entrada inválida.")
        elif opcion == "4":
            try:
                # Seleccionar hogar y dispositivo
                hogares = mostrar_lista_hogares()
                if not hogares:
                    continue
                id_hogar = seleccionar_hogar(hogares)
                if not id_hogar:
                    continue
                dispositivos = mostrar_lista_dispositivos(id_hogar)
                if dispositivos:
                    disp = seleccionar_dispositivo(dispositivos)
                    if disp and dispositivo_dao.eliminar(disp.id_dispositivo):
                        print("Eliminado.")
                    else:
                        print("No encontrado o error.")
            except ValueError:
                print("Entrada inválida.")
        elif opcion == "5":
            try:
                # Mostrar lista de usuarios
                usuarios = usuario_dao.obtener_todos()
                if not usuarios:
                    print("No hay usuarios.")
                    continue
                print("Usuarios disponibles:")
                for idx, usr in enumerate(usuarios, 1):
                    print(
                        f"{idx}. ID: {usr.id_usuario}, Nombre: {usr.perfil.nombre}")
                opcion = int(input("Seleccione número de usuario: "))
                if 1 <= opcion <= len(usuarios):
                    usuario = usuarios[opcion - 1]
                    nuevo_rol = input("Nuevo rol (admin/estandar): ")
                    if nuevo_rol in ["admin", "estandar"]:
                        usuario.rol = nuevo_rol
                        if usuario_dao.actualizar(usuario):
                            print("Rol cambiado.")
                        else:
                            print("Error al cambiar rol.")
                    else:
                        print("Rol inválido.")
                else:
                    print("Opción inválida.")
            except ValueError:
                print("Entrada inválida.")
        elif opcion == "6":
            break
        else:
            print("Opcion invalida.")


def main():
    """Menú principal del sistema SmartHome."""
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
