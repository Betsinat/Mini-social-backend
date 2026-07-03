from fastapi import APIRouter
from app.schemas.user import userCreate

router = APIRouter()

@router.post("/users")
def create_user(user: userCreate):
    return user