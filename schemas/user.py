from pydantic import BaseModel , EmailStr

class userCreate(BaseModel):
    username : str
    email: str
    age: str

#what the server responds
class userResponse(BaseModel):
    id: int
    username:str
    email:str

    class Config:
        from_attributes = True