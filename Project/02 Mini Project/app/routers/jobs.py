from fastapi import APIRouter
from typing import Optional

router = APIRouter(
  prefix='/jobs',
  tags=["Jobs"]
)

jobs = [
  {
    "title":"Backend Developer",
    "company":"Codeaza Technologies",
    "salary":8000000,
    "location":"Rawalpindi"
  },
  {
    "title":"AI Engineer",
    "company":"Open AI",
    "salary":1200000,
    "location":"Los Angeles"
  }
]

@router.get('/get-jobs')
def getJobs():
  return jobs

@router.get("/find-job")
def search_job(
  location:Optional[str] = None,
  company:Optional[str] = None
):
  if location or company:
    for job in jobs:
      if job["location"].lower() == location.lower() or job["company"].lower() == company.lower():
        return job;
  
