from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

from fastapi_pagination.ext.sqlalchemy import paginate

from task.models.task import Task
from task.schemas.task import TaskRequestSchema, TaskRequestPartialSchema
from core.dependencies import get_db
from core.exceptions import NotFound


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
        return paginate(
            self.db,
            select(Task).order_by(Task.id)
        )

    def update_task(self, id: int, task: TaskRequestSchema) -> Task:
        updated_data = task.model_dump(exclude_unset=True)
        return self._update_task_handler(id, updated_data)

    def update_partial_task(self, id: int, task: TaskRequestPartialSchema) -> Task:
        updated_data = task.model_dump(exclude_unset=True)
        return self._update_task_handler(id, updated_data)

    def _update_task_handler(self, id: int, updated_task: dict) -> Task:
        instance: Task = self.find_task_by_id(id)

        for key, value in updated_task.items():
            setattr(instance, key, value)

        self.db.commit()
        self.db.refresh(instance)

        return instance

    def delete_task_by_id(self, id: int) -> None:
        instance: Task = self.find_task_by_id(id)
        self.db.delete(instance)
        self.db.commit()


def get_task_service(db: Session = Depends(get_db)) -> TaskService:
    return TaskService(db)
