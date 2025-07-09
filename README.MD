# CRUD de Artistas con FastAPI, MySQL y SQLAlchemy

Este proyecto es una API para gestionar artistas, álbumes y canciones usando FastAPI, MySQL y SQLAlchemy.

## Requisitos
- Python 3.8+
- MySQL
- pip

## Instalación
1. Clona el repositorio:
   ```bash
   git clone <URL-del-repo>
   cd <carpeta-del-repo>
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Configura tu base de datos en `utils/database.py` (no subas contraseñas reales a GitHub).

## Uso
1. Ejecuta el servidor:
   ```bash
   uvicorn main:app --reload
   ```
2. Accede a la documentación interactiva en: [http://localhost:8000/docs](http://localhost:8000/docs)

## Estructura del proyecto
- `main.py`: Punto de entrada de la aplicación.
- `app/routes.py`: Rutas de la API.
- `models/models.py`: Modelos de SQLAlchemy.
- `schemas/schemas.py`: Esquemas de Pydantic.
- `utils/database.py`: Configuración de la base de datos.

## Licencia
MIT
