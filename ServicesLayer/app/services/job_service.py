from app.database.jobs import jobs
from fastapi import status

def create_job(job):
  new_job={
    "id":len(jobs)+1,
    **job.model_dump()
  }
  jobs.append(new_job)
  return new_job

def get_jobs():
  return jobs;

def update_job(jobId,Job):
  for job in jobs:
    if job["id"] == jobId:
      job.update(Job);
      return {
        "message":"Job updated Successfully"
      }

def delete_job(jobId):
  for job in jobs:
    if job["id"] == jobId:
      jobs.remove(job)
      return {
        "message":"Resource Deleted Successfully.",
        "status_code":status.HTTP_204_NO_CONTENT
      }
    