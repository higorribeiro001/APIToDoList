import uvicorn
from tasks.routers import tasks
from fastapi import FastAPI
from shared.database import engine, Base
from shared.exceptions import NotFound
from shared.exceptions_handler import not_found_exception_handler

app = FastAPI()

app.include_router(tasks.router)
app.add_exception_handler(NotFound, not_found_exception_handler)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)