from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import PostCreate, PostInDB
from ..services.post_service import create_post
from ..dependencies import get_current_user_dependency

router = APIRouter()

@router.post("/add_post", response_model=PostInDB)
async def add_post(post_create: PostCreate, current_user = Depends(get_current_user_dependency), db: Session = Depends(get_db)):
    return create_post(db, post_create, user_id=current_user.id)
