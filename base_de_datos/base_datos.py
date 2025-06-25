import sqlite3
# Nombre de la base de datos
DB_NAME = 'base_de_datos.db'
# Inicializa la base de datos
def inicializar_bd():
    # Crea las tablas si no existen
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS personajes (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            especie TEXT,
            origen TEXT,
            estado TEXT,
            usuario_id INTEGER,
            FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
        )
    ''')
    conn.commit()
    conn.close()

# Llama a la función al importar el módulo
inicializar_bd()

def conectar():
    # Conecta a la base de datos
    return sqlite3.connect(DB_NAME)

# Funciones para usuarios 

def agregar_usuario(nombre, email):
    # Agrega un usuario y retorna su id
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nombre, email) VALUES (?, ?)', (nombre, email))
    conn.commit()
    usuario_id = cursor.lastrowid
    conn.close()
    return usuario_id

def obtener_usuario_por_id(usuario_id):
    # Obtiene un usuario por su id
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT id, nombre, email FROM usuarios WHERE id = ?', (usuario_id,))
    usuario = cursor.fetchone()
    conn.close()
    return usuario

def listar_usuarios():
    # Lista todos los usuarios
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT id, nombre, email FROM usuarios')
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

# Funciones para personajes

def agregar_personaje(personaje, usuario_id):
    # Agrega un personaje asociado a un usuario
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO personajes (id, nombre, especie, origen, estado, usuario_id) VALUES (?, ?, ?, ?, ?, ?)',
        (personaje.id, personaje.nombre, personaje.especie, personaje.origen, personaje.estado, usuario_id)
    )
    conn.commit()
    conn.close()

def obtener_personaje_por_id(personaje_id):
    # Obtiene un personaje por su id
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT id, nombre, especie, origen, estado, usuario_id FROM personajes WHERE id = ?', (personaje_id,))
    personaje = cursor.fetchone()
    conn.close()
    return personaje

def listar_personajes_por_usuario(usuario_id):
    # Lista todos los personajes de un usuario
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT id, nombre, especie, origen, estado FROM personajes WHERE usuario_id = ?', (usuario_id,))
    personajes = cursor.fetchall()
    conn.close()
    return personajes

def actualizar_personaje(personaje_id, nombre=None, especie=None, origen=None, estado=None):
    # Actualiza un personaje    
    conn = conectar()
    cursor = conn.cursor()
    campos = []
    valores = []
    if nombre:
        campos.append("nombre = ?")
        valores.append(nombre)
    if especie:
        campos.append("especie = ?")
        valores.append(especie)
    if origen:
        campos.append("origen = ?")
        valores.append(origen)
    if estado:
        campos.append("estado = ?")
        valores.append(estado)
    if campos:  # Solo ejecuta si hay campos a actualizar
        valores.append(personaje_id)
        cursor.execute(f'UPDATE personajes SET {", ".join(campos)} WHERE id = ?', valores)
        conn.commit()
    conn.close()

def eliminar_personaje(personaje_id):
    # Elimina personajes 
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM personajes WHERE id = ?', (personaje_id,))
    conn.commit()
    conn.close()