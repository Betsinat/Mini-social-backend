from fastapi import APIRouter , Depends , HTTPException , status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from db.database import get_db
from db.models import User
from schemas.user import userCreate, userResponse
from auth.hash import hash_password , verify_password
from auth.jwt import create_access_token

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

@router.post("/login")
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.username == form_data.username).first()
    
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    access_token = create_access_token(data={"sub": str(user.id)})
    
  
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


   
