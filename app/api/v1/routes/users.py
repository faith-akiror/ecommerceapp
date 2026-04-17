from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.dependencies import get_db, require_role
from app.crud.user import user_crud
from app.schemas.user import UserCreate, UserResponse

router = APIRouter()

# ADMIN ONLY
@router.post("/", response_model=UserResponse, dependencies=[Depends(require_role("admin"))])
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    return user_crud.create(db, user_in.model_dump())

@router.get("/", response_model=List[UserResponse], dependencies=[Depends(require_role("admin"))])
def get_users(db: Session = Depends(get_db)):
    return user_crud.get_all(db)

@router.get("/{user_id}", response_model=UserResponse, dependencies=[Depends(require_role("admin"))])
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_crud.get(db, user_id)
    if not user:
        raise HTTPException(404, "User not found")
    return user

@router.put("/{user_id}", response_model=UserResponse, dependencies=[Depends(require_role("admin"))])
def update_user(user_id: int, user_in: UserCreate, db: Session = Depends(get_db)):
    user = user_crud.get(db, user_id)
    return user_crud.update(db, user, user_in.model_dump())

@router.delete("/{user_id}", response_model=UserResponse, dependencies=[Depends(require_role("admin"))])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = user_crud.get(db, user_id)
    return user_crud.delete(db, user)