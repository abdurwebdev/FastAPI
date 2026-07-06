from app.database.database import Base
from sqlalchemy import Column,Integer,String,Boolean

class Job(Base):
  __tablename__ = "jobs"
  id = Column(Integer,primary_key = True,index= True)
  title = Column(String(100))
  company = Column(String(100))
  salary = Column(Integer)
  is_remote = Column(Boolean)
  experience = Column(Integer)
  
  