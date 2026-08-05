from fastapi import APIRouter , Depends , HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.user import userCreate , userResponse
from users import service

router = APIRouter(prefix="/users", tags=["Users"])

# Define the POST route for creating a user;
@router.post("/", response_model=userResponse, status_code=201)
def create_new_user(user: userCreate, db: Session = Depends(get_db)):
   
    return service.create_user(db=db, user=user)

# Define the GET route for looking up a user by their unique ID
@router.get("/{user_id}", response_model=userResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = service.get_user_by_id(db=db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user