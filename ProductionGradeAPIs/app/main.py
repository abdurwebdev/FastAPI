from fastapi import FastAPI
from app.routers.health import router as health_router
from app.routers.jobs import router as job_router

app = FastAPI();

app.include_router(health_router)


@app.get("/")
def home():
  return{
    "message":"Welcome to Codeaza Technologies"
  }