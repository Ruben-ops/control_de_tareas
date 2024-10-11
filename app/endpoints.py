
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models import ControlDTO, TaskControlRepository
from db import get_db
from uow import UnitOfWork
from commands import CreateControlCommand, UpdateControlCommand, DeleteControlCommand

app = FastAPI()

@app.post("/api/v1/controls/", response_model=ControlDTO)
def create_control(control: ControlDTO, db: Session = Depends(get_db)):
    with UnitOfWork(db) as uow:
        command = CreateControlCommand(control.dict(), uow.control_repository)
        return command.execute()

@app.put("/api/v1/controls/{control_id}", response_model=ControlDTO)
def update_control(control_id: int, control_data: ControlDTO, db: Session = Depends(get_db)):
    with UnitOfWork(db) as uow:
        command = UpdateControlCommand(control_id, control_data.dict(), uow.control_repository)
        return command.execute()

@app.delete("/api/v1/controls/{control_id}")
def delete_control(control_id: int, db: Session = Depends(get_db)):
    with UnitOfWork(db) as uow:
        command = DeleteControlCommand(control_id, uow.control_repository)
        try:
            return command.execute()
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))


