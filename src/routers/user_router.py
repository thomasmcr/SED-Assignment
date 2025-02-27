from fastapi import APIRouter
from src.models import RegisterUserModel

router = APIRouter()

@router.post("/register", tags=["User"])
async def create_user(user: RegisterUserModel):
    #TODO: create user in database and hash password
    return user