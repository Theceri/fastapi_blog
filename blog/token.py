from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
from . import schemas

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "014be7e9c2734c4063d0036da3cd05c9321e2ecd48305a5a9e473df4c00e36bb"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email = email)
    except JWTError:
        raise credentials_exception