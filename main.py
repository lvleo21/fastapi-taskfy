from fastapi import FastAPI
from fastapi_pagination import add_pagination

from task.views.v1 import tasks
from core.exceptions import NotFound
from core.exceptions_handler import not_found_exception_handler
from core.settings import settings
from core.redis import lifespan as redis_lifespan


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url="/openapi.json",
    lifespan=redis_lifespan,
    docs_url="/",
    version=settings.TASKFY_VERSION
)

app.router.include_router(tasks.router)
app.add_exception_handler(NotFound, not_found_exception_handler)
add_pagination(app)
