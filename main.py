import uvicorn

from fastapi import FastAPI

from task.routers import tasks


app = FastAPI()
app.router.include_router(tasks.router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
