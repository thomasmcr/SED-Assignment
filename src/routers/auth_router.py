from fastapi import APIRouter, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext 
from src.database.core import SessionDep

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()

@router.post("/token", tags=["Auth"])
async def login(session: SessionDep, response: Response, form_data: OAuth2PasswordRequestForm = Depends()):
    #Get user using form_data.username 
    #Compare password hashes 
    #Issue JWT if they exist
    #Else return 400, incorrect username or password
    response.set_cookie("access_token", "user-id"); 
    #Maybe look if its better to just set the cookie
    return {"access_token": "user-id", "token_type": "bearer"} 
    