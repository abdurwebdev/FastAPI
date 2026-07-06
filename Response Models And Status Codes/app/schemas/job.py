from pydantic import BaseModel,Field
from typing import Optional

class CreateJob(BaseModel):
  title:str=Field(...,min_length=3,max_length=30)
  company:str
  role:str
  salary:int
  is_remote:bool
  
class ResponseJob(BaseModel):
  id:int
  title:str
  company:str
  is_remote:bool
  
