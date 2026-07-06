from sqlalchemy import Column,Integer,String,Boolean

from app.database.database import Base

class Job(Base):
  __tablename__="jobs"
  id = Column(Integer,primary_key = True,index=True)
  title = Column(String(100))
  company = Column(String(100))
  location = Column(String)
  salary = Column(Integer)
  is_remote = Column(Boolean)
  experience = Column(Integer)