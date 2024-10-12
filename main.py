from fastapi import FastAPI
from app.endpoints import router as control_router  

app = FastAPI()

app.include_router(control_router, prefix="/api/v1")
