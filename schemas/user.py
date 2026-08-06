from pydantic import BaseModel, EmailStr
#what client sends
class userCreate(BaseModel):
    email: EmailStr
    password: str
    username: str

# what the server responds
class userResponse(BaseModel):
    id: int
    email: EmailStr
    username : str

    model_config = {
        "from_attributes": True
    }