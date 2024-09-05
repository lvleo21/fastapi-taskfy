import uvicorn

from fastapi import FastAPI

from task.routers import tasks
from shared.exceptions import NotFound
from shared.exceptions_handler import not_found_exception_handler


app = FastAPI()
app.router.include_router(tasks.router)
app.add_exception_handler(NotFound, not_found_exception_handler)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
