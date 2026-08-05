from pydantic import BaseModel, EmailStr

class userCreate(BaseModel):
    email: EmailStr
    password: str

# what the server responds
class userResponse(BaseModel):
    id: int
    email: EmailStr

    model_config = {
        "from_attributes": True
    }