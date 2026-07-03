from fastapi import APIRouter

router = APIRouter(
  tags = ["Jobs"]
)

@router.get("/health_check")
def health():
  return {
    "health":"Helth Ok"
  }
  
