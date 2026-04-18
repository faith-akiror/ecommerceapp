from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.core.dependencies import get_db
from app.core.security import verify_password, create_token
from app.crud.user import user_crud

router = APIRouter()

@router.post("/register")
def register(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = user_crud.get_by_email(db, form.username)
    if user:
        raise HTTPException(400, "User already exists")

    return user_crud.create(db, {
        "email": form.username,
        "password": form.password,
        "role": "customer"
    })


@router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = user_crud.get_by_email(db, form.username)

    if not user or not verify_password(form.password, user.password):
        raise HTTPException(401, "Invalid credentials")

    token = create_token({"sub": user.email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }