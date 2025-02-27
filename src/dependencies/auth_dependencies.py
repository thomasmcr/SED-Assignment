from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from src.database.core import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def fake_decode_token(token):
    #Decode and verify the JWT token, get the user and query the DB for the user
    return User(id=0, username=f"{token}fakedecoded", email="example@email.com", is_admin=False)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user: User = fake_decode_token(token)
    if not user: 
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return {"user": user}
