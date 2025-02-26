from fastapi import APIRouter
from passlib.context import CryptContext 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()

