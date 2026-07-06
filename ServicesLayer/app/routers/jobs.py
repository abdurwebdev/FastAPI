from fastapi import APIRouter
from app.schemas.job import ResponseJob
from fastapi import status
from app.services import job_service
from app.schemas.job import CreateJob
from fastapi import status

router = APIRouter(
  prefix="/api/job",
  tags=["jobs"]
)


@router.post("/create_job",response_model = ResponseJob,status_code = status.HTTP_201_CREATED )
def create_job(Job:CreateJob):
  return job_service.create_job(Job)

@router.get("/get_jobs")
def get_jobs():
  return job_service.get_jobs();

@router.put("/update-job/{jobId}",status_code = status.HTTP_200_OK)
def update_job(jobId:int,Job:CreateJob):
  return job_service.update_job(jobId,Job)
    
    
@router.delete("delete/{jobId}",status_code = status.HTTP_204_NO_CONTENT)
def delete(jobId:int):
  return job_service.delete_job(jobId)
