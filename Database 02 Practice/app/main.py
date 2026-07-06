from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from app.database.database import Base
from app.database.database import engine
from app.database.database import SessionLocal
from app.models.jobs import Job
from app.database.database import get_db
from fastapi import Depends
app = FastAPI()

try:
  Base.metadata.create_all(bind=engine)
  
  db = SessionLocal();
  
  print("Connected To Database")
  
  db.close();
except Exception as e:
  print("Error connecting to database!")
  print(e)
  
@app.get("/")
def home(db:Session = Depends(get_db)):
  return{
    "message":"Welcome to Codeaza Technologies."
  }