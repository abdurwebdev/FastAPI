from sqlalchemy import Column,ARRAY,String,Integer
from app.database.database import Base

class Quote(Base):
  __tablename__ = "quotes"
  id = Column(Integer,primary_key = True,index = True)
  quotetitle = Column(String)
  quoteauthor = Column (String)
  tags = Column(ARRAY(String))
