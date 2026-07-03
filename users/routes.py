from fastapi import APIRouter
from schemas.user import userCreate
from fastapi import Query


router = APIRouter()

@router.post("/users")
def create_user(user: userCreate):
    return user

@router.get("/greet/{username}")
def greet_user(username: str, loud: bool = False):
    if loud:
        return {"message": f"Hello{username.upper()}!"}
    return {"message": f"Hello{username}"}
            
