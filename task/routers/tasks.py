from fastapi import APIRouter, Depends

from typing import List

from task.schemas.task import TaskRequestSchema, TaskResponseSchema, TaskRequestPartialSchema
from task.services.task import get_task_service, TaskService


router = APIRouter(prefix="/tasks")


@router.get("", response_model=List[TaskResponseSchema])
def get_all_tasks_router(
    service: TaskService = Depends(get_task_service),
) -> List[TaskResponseSchema]:
    return service.get_all_tasks()


@router.get("/{task_id}", response_model=List[TaskResponseSchema])
def get_task_by_id_router(
    task_id: int, service: TaskService = Depends(get_task_service)
) -> TaskResponseSchema:
    return service.find_task_by_id(task_id)


@router.post("", response_model=TaskResponseSchema, status_code=201)
def create_task_router(
    task: TaskRequestSchema, service: TaskService = Depends(get_task_service)
) -> TaskResponseSchema:
    return service.create_task(task)


@router.put("/{task_id}", response_model=TaskResponseSchema, status_code=200)
def put_task_router(
    task_id: int,
    task: TaskRequestSchema,
    service: TaskService = Depends(get_task_service),
) -> TaskResponseSchema:
    return service.update_task(task_id, task)


@router.patch("/{task_id}", response_model=TaskResponseSchema, status_code=200)
def patch_task_router(
    task_id: int,
    task: TaskRequestPartialSchema,
    service: TaskService = Depends(get_task_service),
) -> TaskResponseSchema:
    return service.update_partial_task(task_id, task)


@router.delete("/{task_id}", status_code=200)
def delete_task_router(
    task_id: int, service: TaskService = Depends(get_task_service)
) -> None:
    service.delete_task_by_id(task_id)
