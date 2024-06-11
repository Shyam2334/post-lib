from fastapi import FastAPI
from .routers import auth

app = FastAPI()

# Include routers
app.include_router(auth.router)
