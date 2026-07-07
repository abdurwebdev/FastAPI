from dotenv import load_dotenv
load_dotenv()
from app.models.quote import Quote
from app.database.database import Base
from app.database.database import engine
from fastapi import FastAPI
from app.routers.quote import router as quote_router

app = FastAPI()

try:
  Base.metadata.create_all(bind =engine )
  print("Database Connected!")
except Exception as e:
  print("Database Connection Failed")
  print(e)

app.include_router(quote_router)

@app.get("/")
def home():
  return{
    "message":"Welcome to Codeaza Jobs"
  }