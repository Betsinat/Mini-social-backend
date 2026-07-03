from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/posts")
def get_posts(limit: int = 10):
    return {"message": f"Returning {limit} posts"}

@router.get("/posts/search")
def search_posts(q:str = ""):
    if not q:
        return {"message" : "No search term provided"}
    return {"message" : f"searching for {q}"}