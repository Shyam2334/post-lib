from fastapi import FastAPI
from .routers import auth, posts

app = FastAPI()

# Include routers
app.include_router(auth.router)
app.include_router(posts.router)