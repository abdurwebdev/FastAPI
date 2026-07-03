from fastapi import FastAPI
from app.routers.job import router as job_router

app = FastAPI()
app.include_router(job_router)

@app.get("/")
def home():
  return{
    "message":"This is home Page."
  }