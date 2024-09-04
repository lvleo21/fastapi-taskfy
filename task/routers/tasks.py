from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from typing import List

from task.models.task import Task
from shared.dependencies import get_db

router = APIRouter(prefix="/tasks")


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

    class ConfigDict:
        from_attributes = True


class TaskRequest(BaseModel):
    title: str = Field(min_length=3, max_length=Task.TITLE_MAX_LENGHT)
    description: str = Field(min_length=3, max_length=Task.DESCRIPTION_MAX_LENGHT)
    completed: bool


@router.get("", response_model=List[TaskResponse])
def get_tasks(db: Session = Depends(get_db)) -> List[TaskResponse]:
    return db.query(Task).all()


@router.post("", response_model=TaskResponse, status_code=201)
def create_tasks(task: TaskRequest, db: Session = Depends(get_db)) -> TaskResponse:

    task = Task(**task.model_dump())

    db.add(task)
    db.commit()
    db.refresh(task)

    return task
