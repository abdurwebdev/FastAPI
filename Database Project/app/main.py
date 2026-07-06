from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from app.models.job import Job
from app.database.database import Base
from app.database.database import engine
from app.routers.job import router as job_router


app = FastAPI()

try:
  Base.metadata.create_all(bind=engine)
  print("Connected to Database")
except Exception as e:
  print("Connection Error!")
  print(e)

app.include_router(job_router)

@app.get("/")
def home():
  return{
    "message":"Welcome to codeaza technologies."
  }