from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel
from typing import Optional
from datetime import date
from sqlalchemy.orm import Session

Base = declarative_base()


class ControlVO(Base):
    __tablename__ = 'control'
    id = Column(Integer, primary_key=True, autoincrement=True)
    task_reference = Column(String(50), nullable=False)
    alum_reference = Column(String(50), nullable=False)
    control_date = Column(Date, nullable=True)
    work_done_quantity_valuation = Column(Integer, nullable=False)
    work_done_quantity_comment = Column(String, nullable=False)
    work_load_valuation = Column(Integer, nullable=False)
    work_load_comment = Column(String, nullable=False)
    difficult_valuation = Column(Integer, nullable=False)
    difficult_comment = Column(String, nullable=False)


class ControlDTO(BaseModel):
    id: Optional[int]
    task_reference: str
    alum_reference: str
    control_date: Optional[date]
    work_done_quantity_valuation: int
    work_done_quantity_comment: str
    work_load_valuation: int
    work_load_comment: str
    difficult_valuation: int
    difficult_comment: str

    class Config:
        from_atributtes = True  


class ControlFactory:
    @staticmethod
    def create_control_vo(data: dict) -> ControlVO:
        return ControlVO(**data)

    @staticmethod
    def create_control_dto(data: dict) -> ControlDTO:
        return ControlDTO(**data)


class ControlService:
    def __init__(self, repository: 'TaskControlRepository'):
        self.repository = repository

    def get_all_controls(self):
        return self.repository.get_all()

    def get_control_by_id(self, control_id: int):
        return self.repository.get_by_id(control_id)

    def create_control(self, control_data: dict):
        control_vo = ControlFactory.create_control_vo(control_data)
        return self.repository.create(control_vo)

    def update_control(self, control_id: int, control_data: dict):
        return self.repository.update(control_id, control_data)

    def delete_control(self, control_id: int):
        control = self.repository.get_by_id(control_id)
        if control:
            self.repository.delete(control)
            return True
        return False


class TaskControlRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(ControlVO).all()

    def get_by_id(self, control_id: int):
        return self.db.query(ControlVO).filter(ControlVO.id == control_id).first()

    def create(self, control: ControlVO):
        self.db.add(control)
        self.db.commit()
        self.db.refresh(control)
        return control

    def delete(self, control: ControlVO):
        self.db.delete(control)
        self.db.commit()

    def update(self, control_id: int, control_data: dict):
        control = self.get_by_id(control_id)
        for key, value in control_data.items():
            setattr(control, key, value)
        self.db.commit()
        return control
