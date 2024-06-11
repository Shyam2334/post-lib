from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models import User
from ..database import get_db
from ..schemas import UserCreate, Token
from ..config import settings
from ..services.auth_service import create_access_token, get_user, get_password_hash
router = APIRouter()

@router.post("/signup", response_model=Token)
async def signup(user_create: UserCreate, db: Session = Depends(get_db)):
    user = get_user(db, email=user_create.email)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user_create.password)
    new_user = User(email=user_create.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(data={"sub": new_user.email}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}