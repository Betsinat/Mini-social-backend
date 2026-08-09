from fastapi import FastAPI
from users.routes import router as users_router
from posts.routes import router as posts_router
from auth.routes import router as auth_router
from db.models import Base
from db.database import engine

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(users_router)
app.include_router(posts_router)
app.include_router(auth_router)

# Basic health check endpoint to verify server responsiveness
@app.get("/ping")
def ping():
    return {"status": "ok"}