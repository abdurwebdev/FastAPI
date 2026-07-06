from pydantic import BaseModel,Field

class CreateJob(BaseModel):
  title:str = Field(...,min=3,max=100)
  company:str
  location:str
  salary:int
  is_remote:bool
  
class ResponseJob(BaseModel):
  id:int
  title:str = Field(...,min=3,max=100)
  company:str
  location:str
  salary:int
  is_remote:bool