import uvicorn

from fastapi import FastAPI
from fastapi_pagination import add_pagination

from task.views import tasks
from shared.exceptions import NotFound
from shared.exceptions_handler import not_found_exception_handler
from shared.settings import settings


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url="/v1/openapi.json"
)

app.router.include_router(tasks.router)
app.add_exception_handler(NotFound, not_found_exception_handler)
add_pagination(app)

if __name__ == "__main__":
    uvicorn.run(
        '__main__:app',
        host=settings.HOST,
        port=settings.PORT,
        reload=True
    )
