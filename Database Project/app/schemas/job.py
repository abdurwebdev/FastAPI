from pydantic import BaseModel,Field

class JobCreate(BaseModel):
  title:str=Field(...,min=3,max=100)
  company:str
  salary:int
  is_remote:bool
  experience:int