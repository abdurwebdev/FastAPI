from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.scrapper.quotescrapper import scarpedata
from app.services.quote import save_data_scrapped,get_data

router = APIRouter(
  prefix = "/api/quote",
  tags = ["Scarpped Data into DB."]
)


@router.post("/scarpe-data")
def create_scrape(db:Session = Depends(get_db)):
  data = scarpedata()
  return save_data_scrapped(data,db)

@router.get("/get-data")
def getData(db:Session = Depends(get_db)):
  return get_data(db)