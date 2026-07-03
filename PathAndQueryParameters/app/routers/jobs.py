# from fastapi import APIRouter
# from typing import Optional

# router = APIRouter(
#   prefix="/jobs",
#   tags=["Jobs"]
# )

# @router.get("/{job_id}")
# def get_job(job_id:int):
#   return{
#     "job_id":job_id
#   }

#Now Returning Fake Job Data

# @router.get("/{job_id}")
# def get_job(job_id:int):
#   return{
#     "id":job_id,
#     "role":"Backend Developer",
#     "company":"Codeaza Technologies"
#   }
  
#Query Parameters

# @router.get("/")
# def get_location(location:str):
#   return{
#     "location":location
#   }


#Optional Query Parameter

# @router.get("/")
# def get_location(location:Optional[str] = None):
#   return{
#     "location":location
#   }

#Multiple query Parameters

# @router.get('/')
# def get_data(
#   location:Optional[str] = None,
#   company:Optional[str] = None
# ):
#   return{
#     "location":location,
#     "company":company
#   }

from fastapi import APIRouter
from typing import Optional

router = APIRouter(
  prefix = '/jobs',
  tags = ["Jobs"]
)

jobs = [
  {
    "id":1,
    "title":"Backend Developer",
    "company":"codeaza Technologies",
    "location":"Rawalpindi"
  },
  {
    "id":2,
    "title":"AI Engineer",
    "company":"Open AI",
    "location":"US Texas"
  }
]

@router.get("/")
def get_all_jobs():
  return jobs

@router.get("/get-job")
def search_job(location:Optional[str] = None):
  if location:
    for job in jobs:
      if job["location"].lower() == location.lower():
        return {
          "id":job["id"],
          "title":job["title"],
          "company":job["company"],
          "location":job["location"]
        }