from fastapi import APIRouter
from src.models import RegisterUserModel

router = APIRouter()

@router.post("/register", tags=["User"])
async def create_user(user: RegisterUserModel):
    return user

@router.post("/login", tags=["User"])
async def user_login():
    return False