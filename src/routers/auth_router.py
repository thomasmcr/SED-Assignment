from fastapi import APIRouter, Depends, Request, Response
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext 
from src.database.core import SessionDep

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()

@router.post("/token", tags=["Auth"])
async def login(session: SessionDep, form_data: OAuth2PasswordRequestForm = Depends()):
    #Get user using form_data.username 
    #Compare password hashes 
    #Issue JWT if they exist
    #Else return 400, incorrect username or password
    return {"access_token": "user-id", "token_type": "bearer"} 
    