## Evaluacion 2 de POO

Desarrollar una aplicación en Python que permita gestionar usuarios y personajes del universo de Rick and Morty, aplicando:
- Programación orientada a objetos (POO)
- Conexión a base de datos (SQLite)
- Operaciones CRUD
- Consumo de API externa
- Deserialización de JSON
- Registro de datos en base de datos

## Estructura del Repositorio
```
.
├── main.py                         # Archivo principal de la aplicación
├── models ── models.py             # Definición de modelos, sus atributos y metodos
├── base_de_datos ── base_datos.py  # Base de datos de la aplicación
├── api ── apiManager.py            # Api utilizada dentro del proyecto
├── controllers ── controllers.py   # Controladores para la interacción entre modelos
├── requirements.txt                # Dependencias del proyecto
└── README.md                       # Documentación del proyecto
```

# Instalacion y uso
1. Clonar repositorio:
    ```bash
    git clone https://github.com/frodox13/RICKYMORTY_POO_FABIO.git
    ```
2. Navegar al Directorio del proyecto:
    ```bash
    cd RICKYMORTY_POO_FABIO
    ```
3. Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```
4. Ejecutar la aplicación:
    ```bash
    python main.py
    ```