from pydantic import BaseModel,Field
from typing import Optional

class JobCreate(BaseModel):
  title:str = Field(...,min_length=3,max_length=100)
  company:str
  location:str
  salary:Optional[int] = None
  is_remote:bool = False,
  experience:int