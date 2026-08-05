from sqlalchemy.orm import session
from db.models import User
from schemas.user import userCreate

#function handling the database write operation for new user
def create_user(db:session , user:userCreate):

# instantiate the SQLAlchemy model object using the incoming data
    db_user = user(
        username = user.username ,
        email = user.email ,
        hashed_password = user.password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#function handling the database read operation to fetch a user by primary key ID
def get_user_by_id(db:session , user_id : int):
    return db.query(user).filter(user.id == user_id).first()
