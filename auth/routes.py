from fastapi import APIRouter , Depends , HTTPException , status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from db.database import get_db
from db.models import User
from schemas.user import userCreate, userResponse
from auth.hash import hash_password

router = APIRouter(prefix = "/auth" , tags =["Auth"])

@router.post("/register" , response_model = userResponse , status_code =status.HTTP_201_CREATED)

def register_user(user: userCreate , db:Session = Depends(get_db)):
    hashed_pwd = hash_password(user.password)
    new_user = User(
        username = user.username,
        email = user.email,
        hashed_password = hashed_pwd
    )

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST ,
            detail = "username or email already registered"
        )
    return new_user


   
