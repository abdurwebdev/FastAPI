from fastapi import APIRouter
from app.schemas.job import JobCreate

router =  APIRouter(
  prefix = "/api/job"
)

@router.post("/create-job")
def create_job(job:JobCreate):
  return{
    "message":"Job Created Successfully",
    "job":job
  }