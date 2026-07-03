from fastapi import APIRouter

router = APIRouter(
  prefix="/jobs",
  tags = ["jobs"]
)

@router.get("/")
def jobs():
  return[
    {
      "title":"Backend Developer",
      "company":"Coodeaza Technologies"
    },
    {
      "role":"AI Engineer",
      "company":"Open AI"
    }
    ]