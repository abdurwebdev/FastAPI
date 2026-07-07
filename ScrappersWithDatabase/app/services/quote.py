from sqlalchemy.orm import Session
from app.models.quote import Quote
from app.models.quote import Quote
from fastapi import HTTPException

def save_data_scrapped(scarpedata,db:Session):
  
  for item in scarpedata:
    existing_job = db.query(Quote).filter(Quote.quotetitle == item["quotetext"])
    if not existing_job:
      
      quote = Quote(
      quotetitle = item["quotetext"],
      quoteauthor = item["quoteauthor"],
      tags = item["tags"]
    )
      db.add(quote)
  db.commit()
  return {
    "message":"Scarpped data successfully"
  }
  
def get_data(db):
  data = db.query(Quote).all()
  if not data:
    raise HTTPException(
      status_code = 404,
      details = "Quotes not found"
    )
  return data