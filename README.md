# Proyecto de Base de Datos con Python

## Descripción
Este proyecto de Python tiene como objetivo aplicar los conceptos de modelado de datos, conectividad, y optimización de bases de datos en la nube para crear una solución de gestión de datos web que simule una aplicación real, optimizando la estructura, las conexiones y el mantenimiento de datos en un entorno de alta concurrencia. 

Este proyecto crea una API REST utilizando FastAPI y SQLAlchemy para interactuar con una base de datos MySQL. La estructura del proyecto está diseñada para promover la modularidad y la escalabilidad.

## Estructura del Proyecto

APIREST_4DB/
├── app/                # Contiene la lógica de la aplicación
│   ├── __init__.py    # Inicializa el paquete app
│   ├── main.py       # Punto de entrada de la aplicación
│   ├── models.py     # Define los modelos de datos
│   ├── database.py   # Contiene las funciones para interactuar con la base de datos
│   └── crud.py       # Define las operaciones CRUD (Create, Read, Update, Delete)
├── venv/               # Entorno virtual
├── requirements.txt  # Lista de dependencias
├── .gitignore         # Ignora archivos no necesarios para el control de versiones
└── README.md          # Este archivo


## Instalación
1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/sanchxyz/APIrest_4DB.git]

2. **Crear un entorno virtual**
    python -m venv venv
    venv\Scripts\activate  

3. **Instalar dependiencias**
    pip install -r requirements.txt

## Uso 
1. **Iniciar la aplicación**
    uvicorn app.main:app --reload
