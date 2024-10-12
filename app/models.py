from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    due_date = Column(DateTime)
    professor_id = Column(Integer, ForeignKey("professors.id"))

    professor = relationship("Professor", back_populates="tasks")
    followups = relationship("Followup", back_populates="task")

class Followup(Base):
    __tablename__ = "followups"
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    student_id = Column(Integer, ForeignKey("students.id"))
    work_done = Column(String)
    difficulty_rating = Column(Integer)
    comments = Column(String)

    task = relationship("Task", back_populates="followups")
    student = relationship("Student", back_populates="followups")

class Professor(Base):
    __tablename__ = "professors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    tasks = relationship("Task", back_populates="professor")

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    followups = relationship("Followup", back_populates="student")

