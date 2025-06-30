from base_de_datos import base_datos as db
from models import models
from controllers import controllers as ctrl

# Menu principal de la aplicación
def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar usuario")
        print("2. Listar usuarios")
        print("3. Buscar usuario por ID")
        print("4. Buscar y asociar personaje por ID (API)")
        print("5. Listar personajes de un usuario")
        print("6. Actualizar personaje")
        print("7. Eliminar personaje")
        print("8. Buscar episodio por ID (API)")
        print("9. Buscar ubicación por ID (API)")
        print("0. Salir")
        opcion = input("Elige una opción: ")

        try:
            if opcion == "1":
                nombre = input("Nombre: ")
                email = input("Email: ")
                if not nombre or not email:
                    print("Nombre y email son obligatorios.")
                    continue
                user_id = ctrl.registrar_usuario(nombre, email)
                print(f"Usuario registrado con ID: {user_id}")

            elif opcion == "2":
                usuarios = ctrl.listar_usuarios()
                if not usuarios:
                    print("No hay usuarios registrados.")
                for u in usuarios:
                    print(f"ID: {u.id}, Nombre: {u.nombre}, Email: {u.email}")

            elif opcion == "3":
                try:
                    uid = int(input("ID de usuario: "))
                except ValueError:
                    print("ID inválido.")
                    continue
                usuario = ctrl.obtener_usuario(uid)
                if usuario:
                    print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Email: {usuario.email}")
                else:
                    print("Usuario no encontrado.")

            elif opcion == "4":
                try:
                    uid = int(input("ID de usuario: "))
                    pid = int(input("ID de personaje (API): "))
                except ValueError:
                    print("ID inválido.")
                    continue
                usuario = ctrl.obtener_usuario(uid)
                if not usuario:
                    print("Usuario no encontrado.")
                    continue
                personaje = ctrl.crear_personaje_desde_api(pid, uid)
                if personaje:
                    print(f"Personaje '{personaje.nombre}' asociado al usuario {uid}.")
                else:
                    print("No se encontró el personaje en la API o ya existe en la base de datos.")

            elif opcion == "5":
                try:
                    uid = int(input("ID de usuario: "))
                except ValueError:
                    print("ID inválido.")
                    continue
                usuario = ctrl.obtener_usuario(uid)
                if not usuario:
                    print("Usuario no encontrado.")
                    continue
                personajes = ctrl.listar_personajes(uid)
                if not personajes:
                    print("El usuario no tiene personajes asociados.")
                for p in personajes:
                    print(f"ID: {p.id}, Nombre: {p.nombre}, Especie: {p.especie}, Origen: {p.origen}, Estado: {p.estado}")

            elif opcion == "6":
                try:
                    pid = int(input("ID de personaje: "))
                except ValueError:
                    print("ID inválido.")
                    continue
                personaje = ctrl.leer_personaje(pid)
                if not personaje:
                    print("Personaje no encontrado.")
                    continue
                nombre = input("Nuevo nombre (deja vacío para no cambiar): ")
                especie = input("Nueva especie (deja vacío para no cambiar): ")
                origen = input("Nuevo origen (deja vacío para no cambiar): ")
                estado = input("Nuevo estado (deja vacío para no cambiar): ")
                ctrl.actualizar_personaje(pid, nombre or None, especie or None, origen or None, estado or None)
                print("Personaje actualizado.")

            elif opcion == "7":
                try:
                    pid = int(input("ID de personaje a eliminar: "))
                except ValueError:
                    print("ID inválido.")
                    continue
                personaje = ctrl.leer_personaje(pid)
                if not personaje:
                    print("Personaje no encontrado.")
                    continue
                ctrl.eliminar_personaje(pid)
                print("Personaje eliminado.")

            elif opcion == "8":
                try:
                    eid = int(input("ID de episodio (API): "))
                except ValueError:
                    print("ID inválido.")
                    continue
                episodio = ctrl.obtener_episodio_api(eid)
                if episodio:
                    print(f"Episodio: {episodio['name']} | Fecha: {episodio['air_date']} | Código: {episodio['episode']}")
                else:
                    print("No se encontró el episodio en la API.")

            elif opcion == "9":
                try:
                    lid = int(input("ID de ubicación (API): "))
                except ValueError:
                    print("ID inválido.")
                    continue
                ubicacion = ctrl.obtener_ubicacion_api(lid)
                if ubicacion:
                    print(f"Ubicación: {ubicacion['name']} | Tipo: {ubicacion['type']} | Dimensión: {ubicacion['dimension']}")
                else:
                    print("No se encontró la ubicación en la API.")

            elif opcion == "0":
                print("Ha salido del programa.")
                break

            else:
                print("Opción no válida.")

        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    menu()
