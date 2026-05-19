from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine
from models import Base, Task
from schemas import TaskCreate
from sqlalchemy.orm import Session
from database import SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Obtener sesión DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "API funcionando 🚀"}


@app.get("/tasks")
def get_tasks():
    db: Session = SessionLocal()
    tasks = db.query(Task).all()
    db.close()
    return tasks


@app.post("/tasks")
def create_task(task: TaskCreate):
    db: Session = SessionLocal()

    new_task = Task(title=task.title)

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    db.close()

    return new_task

@app.delete('/tasks/{task_id}')
def delete_task(task_id: int):
    db: Session = SessionLocal()

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        return {'error': 'Task no encontrada'}

    db.delete(task)
    db.commit()

    db.close()

    return {'message': 'Task eliminada'}

