from fastapi import Request, HTTPException, Security, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
import os
from config import config

# Security scheme for bearer token
security = HTTPBearer()

def verify_jwt(token: str) -> dict:
    """
    Verifies and decodes a JWT token.
    """
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=config.ALGORITHM)
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

def authenticate_user(credentials: HTTPAuthorizationCredentials = Security(security)):
    """
    Middleware function to authenticate a user via JWT.
    """
    return verify_jwt(credentials.credentials)
