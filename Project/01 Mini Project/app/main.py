from fastapi import FastAPI
from app.routers.users import router as user_router
from app.routers.jobs import router as job_router
from app.routers.health import router as health_router

app = FastAPI();
app.include_router(user_router)
app.include_router(job_router)
app.include_router(health_router)

@app.get("/")
def home():
  return{
    "message":"Welcome To Codeaza Technologies"
  }