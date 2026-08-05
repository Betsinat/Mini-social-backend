from fastapi import FastAPI
from users.routes import router as users_router
from posts.routes import router as posts_router

app = FastAPI()

app.include_router(users_router)
app.include_router(posts_router)

# Basic health check endpoint to verify server responsiveness
@app.get("/ping")
def ping():
    return {"status": "ok"}