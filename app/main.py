from fastapi import FastAPI
from app.routers import tasks, users
from app.database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(tasks.router)
app.include_router(users.router)

