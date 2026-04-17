from fastapi import Depends, HTTPException
from jose import jwt
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.user import User
import os

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

def get_current_user(token: str, db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")])
        email = payload.get("sub")
    except:
        raise HTTPException(401,"Invalid token")

    user = db.query(User).filter_by(email=email).first()
    if not user:
        raise HTTPException(404,"User not found")
    return user

def require_role(role:str):
    def wrapper(user=Depends(get_current_user)):
        if user.role!=role:
            raise HTTPException(403,"Forbidden")
        return user
    return wrapper