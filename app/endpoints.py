from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models import ControlDTO, ControlVO
from db import get_db
from uow import UnitOfWork

app = FastAPI()

@app.post("/api/v1/controls/", response_model=ControlDTO)
def create_control(control: ControlDTO, db: Session = Depends(get_db)):
    with UnitOfWork(db) as uow:
        control_vo = ControlVO(**control.dict())
        return uow.control_repository.create(control_vo)

@app.get("/api/v1/controls/", response_model=List[ControlDTO])
def get_all_controls(db: Session = Depends(get_db)):
    with UnitOfWork(db) as uow:
        return uow.control_repository.get_all()

@app.get("/api/v1/controls/{control_id}", response_model=ControlDTO)
def get_control_by_id(control_id: int, db: Session = Depends(get_db)):
    with UnitOfWork(db) as uow:
        control = uow.control_repository.get_by_id(control_id)
        if control is None:
            raise HTTPException(status_code=404, detail="Control not found")
        return control

@app.put("/api/v1/controls/{control_id}", response_model=ControlDTO)
def update_control(control_id: int, control_data: ControlDTO, db: Session = Depends(get_db)):
    with UnitOfWork(db) as uow:
        control_vo = uow.control_repository.update(control_id, control_data.dict())
        return control_vo

@app.delete("/api/v1/controls/{control_id}")
def delete_control(control_id: int, db: Session = Depends(get_db)):
    with UnitOfWork(db) as uow:
        control = uow.control_repository.get_by_id(control_id)
        if control is None:
            raise HTTPException(status_code=404, detail="Control not found")
        uow.control_repository.delete(control)
        return {"message": "Control deleted"}

