from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: datetime

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    professor_id: int

    class Config:
        orm_mode = True

class FollowupBase(BaseModel):
    work_done: str
    difficulty_rating: int
    comments: Optional[str] = None

class FollowupCreate(FollowupBase):
    task_id: int
    student_id: int

class Followup(FollowupBase):
    id: int
    task_id: int
    student_id: int

    class Config:
        orm_mode = True

class ProfessorBase(BaseModel):
    name: str

class ProfessorCreate(ProfessorBase):
    pass

class Professor(ProfessorBase):
    id: int
    tasks: List[Task] = []

    class Config:
        orm_mode = True

class StudentBase(BaseModel):
    name: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    followups: List[Followup] = []

    class Config:
        orm_mode = True
