from sqlalchemy.orm import Session
from .models import TaskControlRepository

class UnitOfWork:
    def __init__(self, db: Session):
        self.db = db
        self.control_repository = TaskControlRepository(db)

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.commit()
        else:
            self.rollback()