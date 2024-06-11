from sqlalchemy.orm import Session
from ..models import Post
from ..schemas import PostCreate

def create_post(db: Session, post: PostCreate, user_id: int):
    db_post = Post(**post.dict(), user_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
