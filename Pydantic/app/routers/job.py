from fastapi import APIRouter
from typing import Optional
from app.schemas.job import JobCreate

router = APIRouter(
  prefix="/job",
  tags=["Jobs"]
)


# @router.post("/create-job")
# def create_job(job:JobCreate):
#   return{
#     "message":"Job created successfully",
#     "job":job
#   }

@router.post("/create-job")
def create_job(job:JobCreate):
  return{
    "title":job.title,
    "company":job.comapny,
    "location":job.location
  }
