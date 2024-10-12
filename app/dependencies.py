from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from .database import Database
from .models import Professor, Student

def get_db():
    db = Database.get_session()()
    try:
        yield db
    finally:
        db.close()

def get_current_professor(db: Session = Depends(get_db), professor_id: int = 1):
    professor = db.query(Professor).filter(Professor.id == professor_id).first()
    if professor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Professor not found")
    return professor

def get_current_student(db: Session = Depends(get_db), student_id: int = 1):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return student

