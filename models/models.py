from api.apiManager import ApiManager
import base_de_datos.base_datos as db

api_manager = ApiManager()

# Clase Usuario que gestiona los personajes
class Usuario:
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

    @staticmethod
    def registrar(nombre, email):
        return db.agregar_usuario(nombre, email)

    @staticmethod
    def obtener_por_id(usuario_id):
        usuario = db.obtener_usuario_por_id(usuario_id)
        if usuario:
            return Usuario(*usuario)
        return None

    @staticmethod
    def listar_usuarios():
        return [Usuario(*u) for u in db.listar_usuarios()]

# Clase Personaje gestionada por usuario
class Personaje:
    def __init__(self, id, nombre, especie, origen, estado, usuario_id=None):
        self.id = id
        self.nombre = nombre
        self.especie = especie
        self.origen = origen
        self.estado = estado
        self.usuario_id = usuario_id

    @staticmethod
    def crear(personaje, usuario_id):
        db.agregar_personaje(personaje, usuario_id)

    @staticmethod
    def leer(personaje_id):
        p = db.obtener_personaje_por_id(personaje_id)
        if p:
            return Personaje(*p)
        return None

    @staticmethod
    def actualizar(personaje_id, nombre=None, especie=None, origen=None, estado=None):
        db.actualizar_personaje(personaje_id, nombre, especie, origen, estado)

    @staticmethod
    def eliminar(personaje_id):
        db.eliminar_personaje(personaje_id)

    @staticmethod
    def listar(usuario_id):
        return [Personaje(*p, usuario_id=usuario_id) for p in db.listar_personajes_por_usuario(usuario_id)]

# Clase RickAndMortyApi que crea personajes
class RickAndMortyApi:
    def __init__(self, api_manager):
        self.api_manager = api_manager

    def obtener_personajes(self, personaje_id):
        return self.api_manager.obtener_personaje_api(personaje_id)

    def deserializar_json(self, json_data):
        return Personaje(
            id=json_data['id'],
            nombre=json_data['name'],
            especie=json_data['species'],
            origen=json_data['origin']['name'],
            estado=json_data['status']
        )

rick_and_morty_api = RickAndMortyApi(api_manager)