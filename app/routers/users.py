from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/followups/", response_model=schemas.Followup)
def create_followup(followup: schemas.FollowupCreate, db: Session = Depends(get_db)):
    return crud.create_followup(db=db, followup=followup)

@router.get("/followups/{task_id}", response_model=List[schemas.Followup])
def read_followups(task_id: int, db: Session = Depends(get_db)):
    followups = crud.get_followups(db, task_id=task_id)
    return followups
