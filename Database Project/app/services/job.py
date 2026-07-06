from app.models.job import Job
from app.schemas.job import JobCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy import func

def create_job(job:JobCreate,db:Session):
  new_job = Job(
    **job.model_dump()
  )
  db.add(new_job)
  db.commit()
  db.refresh(new_job)
  return new_job
  
def getjobs(db:Session):
  return db.query(Job).all()

def getone_job(jobId,db:Session):
  job = db.query(Job).filter(Job.id == jobId).first()
  
  if not job:
    raise HTTPException(
      status_code = 404,
      detail = "Job Not Found."
    )
  return job

def update_job(jobId:int,job:JobCreate,db:Session):
  existingjob = db.query(Job).filter(Job.id == jobId).first()
  
  if not existingjob:
    raise HTTPException(
      status_code = 404,
      detail = "Job not found."
    )
  for key,values in job.model_dump().items():
    setattr(existingjob,key,values)
  db.commit();
  db.refresh(existingjob)
  return existingjob
  
def delete_job(jobId:int,db:Session):
  job = db.query(Job).filter(Job.id == jobId).first()
  
  if not job:
    raise HTTPException(
      status_code = 404,
      detail = "Job Deleted Successfully"
    )
  
  db.delete(job)
  db.commit()
  
def getjob_by_company(company:str,db:Session):
  job = db.query(Job).filter(func.lower(Job.company) == company.lower()).first();
  if not job:
    raise HTTPException(
      status_code = 404,
      detail = "Job not found"
    )
  return job