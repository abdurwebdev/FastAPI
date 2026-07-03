from fastapi import APIRouter


router = APIRouter(
  prefix = '/jobs',
  tags = ['Jobs']
)

@router.get("/")
def job():
  return [
    {
      "title":"Backend Developer",
      "company":"Codeaza Technologies"
    },
    {
      "title":"AI Engineer",
      "company":"Open AI"
    }
  ]
