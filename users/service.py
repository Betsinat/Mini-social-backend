from sqlalchemy.orm import Session
from db.models import User
from schemas.user import userCreate

# function handling the database write operation for a new user
def create_user(db: Session, user: userCreate):
    db_user = User(
        email=user.email,
        hashed_password=user.password,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# function handling the database read operation to fetch a user by primary key ID
def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
