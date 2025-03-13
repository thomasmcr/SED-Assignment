from dotenv import load_dotenv
from src.handlers.auth_redirect_handler import AuthRedirect
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from src.database.core import User
import jwt, os

load_dotenv()

CREDENTIALS_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid authentication credentials",
    headers={"WWW-Authenticate": "Bearer"}
)
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl="token", auto_error=False)

#Get and return the user id from the token
def decode_token(token) -> int:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return 123 
    except:
        return None; 

#Get the user from the db based on a userID
def authenticate_user(user_id: str) -> User | None:
    #Query db for user and return user or none
    return User(id=0, username=f"test", email="test@email.com", is_admin=False)

#Dependency to be used in api endpoints, either gets the current user or throws a 401
async def get_current_user(token: str = Depends(OAUTH2_SCHEME)):
    user_id = decode_token(token)
    if user_id is None: 
        raise CREDENTIALS_EXCEPTION
    user: User = authenticate_user(user_id)
    if not user: 
        raise CREDENTIALS_EXCEPTION
    return user 

#Dependency to be used in page endpoints, either gets the current user or redirects
async def get_current_user_redirect(token: str = Depends(OAUTH2_SCHEME)):
    user_id = decode_token(token)
    if user_id is None: 
        raise AuthRedirect
    user: User = authenticate_user(user_id)
    if not user: 
        raise AuthRedirect
    return user 


