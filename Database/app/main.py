from fastapi import FastAPI

from dotenv import load_dotenv
load_dotenv();
from app.database.database import Base
from app.database.database import engine
from app.database.database import SessionLocal




app = FastAPI()

try:
  
  Base.metadata.create_all(bind=engine)

  db = SessionLocal()

  print("Database connected successfully")

  db.close()
except Exception as e:
  print("Database Connection Failed")
  print(e)


@app.get("/")
def home():
  return{
    "message":"Welcome to Codeaza Technologies."
  }