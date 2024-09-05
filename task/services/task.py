from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from task.models.task import Task
from task.schemas.task import TaskRequestSchema
from shared.dependencies import get_db
from shared.exceptions import NotFound


class TaskService:
    def __init__(self, db: Session) -> None:
        self.db: Session = db

    def find_task_by_id(self, id: int) -> Task:
        task: Task = self.db.get(Task, id)

        if task is None:
            raise NotFound("task")

        return task

    def create_task(self, task: TaskRequestSchema) -> Task:
        task: Task = Task(**task.model_dump())
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def get_all_tasks(self) -> List[Task]:
        return self.db.query(Task).all()

    def update_task(self, id: int, task: TaskRequestSchema) -> Task:
        instance: Task = self.find_task_by_id(id)
        instance.title = task.title
        instance.description = task.description
        instance.completed = task.completed

        self.db.commit()
        self.db.refresh(instance)

        return instance

    def delete_task_by_id(self, id: int) -> None:
        instance: Task = self.find_task_by_id(id)
        self.db.delete(instance)
        self.db.commit()


def get_task_service(db: Session = Depends(get_db)) -> TaskService:
    return TaskService(db)
