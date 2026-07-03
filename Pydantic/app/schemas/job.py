from pydantic import BaseModel,Field
from typing import Optional

class JobCreate(BaseModel):
  title:str = Field(...,min_length=3,max_length=100)
  comapny:str
  location:str
  salary:Optional[int] = None