from fastapi import APIRouter,HTTPException
from app.schemas.job import JobCreate

router = APIRouter(
  prefix="/api"
)

jobs = []
#readJobs

@router.get("/get-jobs")
def get_all_jobs():
  return jobs

#Create Jobs
@router.post("/create-job")
def createjob(job:JobCreate):
  new_job = {
    "id":len(jobs)+1,
    **job.model_dump()
  }
  jobs.append(new_job)
  return{
    "message":"Job added successfully",
    "job":new_job
  }
  
#Update Job

@router.put("/{jobId}")
def updatejob(jobId:int,updated_job:JobCreate):
  for job in jobs:
    if job["id"] == jobId:
      job.update(updated_job.model_dump())
      return {
        "message":"Job updated successfully",
        "job":job
      }
  raise HTTPException(
    status_code = 404,
    detail = "Job not found."
  )
  
#Read One Job

@router.get("/{jobId}")
def getspecificjob(jobId:int):
  for job in jobs:
    if job["id"] == jobId:
      return job
  raise HTTPException(
    status_code = 404,
    detail = "Job not found."
  )

# Delete a job

@router.delete("/delete-job/{jobId}")
def deletejob(jobId:int):
  for job in jobs:
    if job["id"] == jobId:
      jobs.remove(job)
      return {
        "message":"Job Deleted Successfully"
      }
  raise HTTPException(
    status_code = 404,
    detail = "Job Not Found."
  )
  
#Search Job by company

@router.get("/get-job/{jobName}")
def search_job(jobName:str):
  for job in jobs:
    if jobName.lower()  == job["company"].lower():
      return{
        "job":job
      } 

@router.get("/get-job/experience/{extime}")
def get_job_by_exp(extime:int):
  for job in jobs:
    if job["experience"] == extime:
      return {
        "jobs":job
      }    
  

  