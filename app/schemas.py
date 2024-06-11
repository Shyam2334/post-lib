from pydantic import BaseModel, EmailStr, constr

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: constr(min_length=6)

class UserInDB(UserBase):
    id: int
    hashed_password: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str

class PostBase(BaseModel):
    text: constr(max_length=1024)

class PostCreate(PostBase):
    pass

class PostInDB(PostBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True