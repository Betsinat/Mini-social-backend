from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class UserCreate(BaseModel):
    username : str
    email: str
    password : str

@app.get("/")
def home():
    return {"message": "Welcome to Mini social platform API"}

@app.get("/health")
def health():
    return {"status" : "healthy"}

@app.post("/register")
def register(user:UserCreate):
    return{
        "message": "User recieved successfully",
        "username": user.username

    }
