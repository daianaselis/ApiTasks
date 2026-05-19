# ApiTasks

API REST de gestión de tareas desarrollada con FastAPI y PostgreSQL.

## Tecnologías

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn

---

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/daianaselis/ApiTasks.git
```

Entrar al proyecto:

```bash
cd ApiTasks
```

Crear entorno virtual:

```bash
python -m venv venv
```

Activar entorno virtual:

### Windows

```bash
venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Configuración de base de datos

Crear una base de datos PostgreSQL llamada:

```text
taskdb
```

Modificar la conexión en `database.py`:

```python
DATABASE_URL = "postgresql+psycopg://postgres:TU_PASSWORD@localhost:5432/taskdb"
```

---

## Ejecutar el proyecto

```bash
uvicorn main:app --reload
```

Servidor:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

## Funcionalidades

- Crear tareas
- Obtener tareas
- Obtener tarea por ID
- Actualizar tareas
- Eliminar tareas

---

## Endpoints

| Método | Endpoint | Descripción |
|---|---|---|
| GET | /tasks | Obtener tareas |
| GET | /tasks/{id} | Obtener tarea |
| POST | /tasks | Crear tarea |
| PUT | /tasks/{id} | Actualizar tarea |
| DELETE | /tasks/{id} | Eliminar tarea |

---

## Autor

Daiana Betsabé Selis