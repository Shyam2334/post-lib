from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import PostCreate, PostInDB
from ..services.post_service import create_post, get_user_posts
from ..dependencies import get_current_user_dependency
from cachetools import TTLCache

router = APIRouter()

# In-memory cache
cache = TTLCache(maxsize=100, ttl=300)

@router.post("/add_post", response_model=PostInDB)
async def add_post(post_create: PostCreate, current_user = Depends(get_current_user_dependency), db: Session = Depends(get_db)):
    return create_post(db, post_create, user_id=current_user.id)

@router.get("/get_posts", response_model=list[PostInDB])
async def get_posts(current_user = Depends(get_current_user_dependency), db: Session = Depends(get_db)):
    user_id = current_user.id
    if user_id in cache:
        return cache[user_id]
    posts = get_user_posts(db, user_id=user_id)
    cache[user_id] = posts
    return posts

@router.delete("/delete_post/{post_id}")
async def delete_post_endpoint(post_id: int, current_user = Depends(get_current_user_dependency), db: Session = Depends(get_db)):
    if not delete_post(db, post_id, user_id=current_user.id):
        raise HTTPException(status_code=404, detail="Post not found")
    return {"detail": "Post deleted"}
