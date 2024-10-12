from sqlalchemy.orm import Session
from app import models, schemas

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Task).offset(skip).limit(limit).all()

def create_task(db: Session, task: schemas.TaskCreate, professor_id: int):
    db_task = models.Task(**task.dict(), professor_id=professor_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_followups(db: Session, task_id: int):
    return db.query(models.Followup).filter(models.Followup.task_id == task_id).all()

def create_followup(db: Session, followup: schemas.FollowupCreate):
    db_followup = models.Followup(**followup.dict())
    db.add(db_followup)
    db.commit()
    db.refresh(db_followup)
    return db_followup
