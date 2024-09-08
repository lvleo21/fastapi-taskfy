from typing import List

from fastapi import APIRouter, Depends

from fastapi_pagination import Page
from fastapi_cache.decorator import cache


from task.schemas.task import (
    TaskRequestSchema,
    TaskResponseSchema,
    TaskRequestPartialSchema,
)
from task.services.task import get_task_service, TaskService


router = APIRouter(prefix="/v1/tasks")


@router.get("", response_model=Page[TaskResponseSchema])
@cache(expire=60)
def get_all_tasks_api_view(
    service: TaskService = Depends(get_task_service),
) -> List[TaskResponseSchema]:
    return service.get_all_tasks()


@router.get("/{task_id}", response_model=List[TaskResponseSchema])
@cache(expire=60)
def get_task_by_id_api_view(
    task_id: int, service: TaskService = Depends(get_task_service)
) -> TaskResponseSchema:
    return service.find_task_by_id(task_id)


@router.post("", response_model=TaskResponseSchema, status_code=201)
def create_task_api_view(
    task: TaskRequestSchema, service: TaskService = Depends(get_task_service)
) -> TaskResponseSchema:
    return service.create_task(task)


@router.put("/{task_id}", response_model=TaskResponseSchema, status_code=200)
def put_task_api_view(
    task_id: int,
    task: TaskRequestSchema,
    service: TaskService = Depends(get_task_service),
) -> TaskResponseSchema:
    return service.update_task(task_id, task)


@router.patch("/{task_id}", response_model=TaskResponseSchema, status_code=200)
def patch_task_api_view(
    task_id: int,
    task: TaskRequestPartialSchema,
    service: TaskService = Depends(get_task_service),
) -> TaskResponseSchema:
    return service.update_partial_task(task_id, task)


@router.delete("/{task_id}", status_code=200)
def delete_task_api_view(
    task_id: int, service: TaskService = Depends(get_task_service)
) -> None:
    service.delete_task_by_id(task_id)
