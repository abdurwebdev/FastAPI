from fastapi import APIRouter

router = APIRouter(
  prefix="/users",
  tags=["users"]
)

@router.get("/")
def users():
  return[
    {
      "name":"Ali",
      "company":"Codeaza Technologies"
    },
    {
      "name":"Abdur-Rehman",
      "company":"Open AI"
    }
  ]