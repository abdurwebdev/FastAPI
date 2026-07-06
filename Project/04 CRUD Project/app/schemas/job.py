from pydantic import BaseModel

class JobCreate(BaseModel):
  title:str
  company:str
  location:str
  salary:int
  is_remote:bool = False
  experience:int