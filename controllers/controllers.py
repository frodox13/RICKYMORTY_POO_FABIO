from models.models import Usuario, Personaje, RickAndMortyApi, rick_and_morty_api

# Controladores para Usuario

def registrar_usuario(nombre, email):
# Registra un nuevo usuario y retorna su id
    return Usuario.registrar(nombre, email)

def obtener_usuario(usuario_id):
# Obtiene un usuario por su id
    return Usuario.obtener_por_id(usuario_id)

def listar_usuarios():
# Lista todos los usuarios
    return Usuario.listar_usuarios()

# Controladores para Personaje

def crear_personaje_desde_api(personaje_id, usuario_id):
# Obtiene un personaje de la API y lo asocia a un usuario
    json_data = rick_and_morty_api.obtener_personajes(personaje_id)
    if json_data:
        personaje = rick_and_morty_api.deserializar_json(json_data)
        Personaje.crear(personaje, usuario_id)
        return personaje
    return None

def leer_personaje(personaje_id):
# Lee un personaje de la base de datos
    return Personaje.leer(personaje_id)

def actualizar_personaje(personaje_id, nombre=None, especie=None, origen=None, estado=None):
# Actualiza los datos de un personaje
    Personaje.actualizar(personaje_id, nombre, especie, origen, estado)

def eliminar_personaje(personaje_id):
# Elimina un personaje de la base de datos
    Personaje.eliminar(personaje_id)

def listar_personajes(usuario_id):
# Lista todos los personajes asociados a un usuario
    return Personaje.listar(usuario_id)