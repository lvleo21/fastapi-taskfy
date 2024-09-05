from pydantic import BaseModel, Field

from task.models.task import Task


class TaskResponseSchema(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

    class ConfigDict:
        from_attributes = True


class TaskRequestSchema(BaseModel):
    title: str = Field(
        min_length=3,
        max_length=Task.TITLE_MAX_LENGHT
    )
    description: str = Field(
        min_length=3,
        max_length=Task.DESCRIPTION_MAX_LENGHT
    )
    completed: bool
