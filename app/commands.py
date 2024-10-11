from abc import ABC, abstractmethod
from fastapi import HTTPException

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

from models import ControlVO, TaskControlRepository


class CreateControlCommand(Command):
    def __init__(self, repository: TaskControlRepository, control_data: dict):
        self.repository = repository
        self.control_data = control_data

    def execute(self):
        control_vo = ControlVO(**self.control_data)
        return self.repository.create(control_vo)



class UpdateControlCommand(Command):
    def __init__(self, repository: TaskControlRepository, control_id: int, control_data: dict):
        self.repository = repository
        self.control_id = control_id
        self.control_data = control_data

    def execute(self):
        return self.repository.update(self.control_id, self.control_data)



class DeleteControlCommand(Command):
    def __init__(self, repository: TaskControlRepository, control_id: int):
        self.repository = repository
        self.control_id = control_id

    def execute(self):
        control = self.repository.get_by_id(self.control_id)
        if control:
            self.repository.delete(control)
            return {"message": "Control deleted"}
        else:
            raise HTTPException(status_code=404, detail="Control not found")


