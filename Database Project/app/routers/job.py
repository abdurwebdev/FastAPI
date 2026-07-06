from fastapi import APIRouter
from fastapi import Depends
from app.database.database import get_db
from sqlalchemy.orm import Session 
from app.services import job as job_service

from app.schemas.job import JobCreate
router = APIRouter(
  prefix = "/api/job",
  tags = ["jobs"]
)

@router.post("/create-job")
def create_job(job:JobCreate,db:Session = Depends(get_db)):
  return job_service.create_job(job,db)
  
@router.get("/get-all-jobs")
def get_all_jobs(db:Session = Depends(get_db)):
  return job_service.getjobs(db)
  
@router.get("/get-one-job/{jobId}")
def getonejob(jobId:int,db:Session = Depends(get_db)):
  return job_service.getone_job(jobId,db)

@router.put("/update-job/{jobId}")
def update_job(jobId:int,job:JobCreate,db:Session= Depends(get_db)):
  return job_service.update_job(jobId,job,db)

@router.delete("/delete/{jobId}")
def delete_job(jobId,db:Session = Depends(get_db)):
  job_service.delete_job(jobId,db)
  
#Mini Challenge

@router.get("/jobs/company/{company}")
def getjob_bycompany(company,db:Session=Depends(get_db)):
  return job_service.getjob_by_company(company,db)