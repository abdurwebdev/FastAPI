from fastapi import APIRouter
from app.schemas.job import CreateJob
from app.schemas.job import ResponseJob
from typing import List
from fastapi import status
from fastapi import Response

router = APIRouter(
  prefix = "/api/job",
  tags=["Jobs"]
)

jobs = []

@router.post("/create-job",response_model = ResponseJob,status_code = status.HTTP_201_CREATED )
def create_job(job:CreateJob):
  new_job = {
    "id":len(jobs)+1,
    **job.model_dump()
  }
  jobs.append(new_job)
  return new_job
  

@router.get("/get-job",response_model=List[ResponseJob])
def get_job():
  return jobs

@router.get("/get_job_by_id/{jobId}",response_model = ResponseJob)
def getjobbyid(jobId:int):
  for job in jobs:
    if job["id"] == jobId:
      return job
  

@router.post("/delete/{jobId}",status_code = status.HTTP_204_NO_CONTENT)
def delete_job(jobId:int):
  for job in jobs:
    if job["id"] == jobId:
      jobs.remove(job)
      return Response(status_code = status.HTTP_204_NO_CONTENT)
  