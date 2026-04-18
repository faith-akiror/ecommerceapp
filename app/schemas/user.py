from pydantic import BaseModel
from typing import Optional
from app.models.user import Role

class UserCreate(BaseModel):
    email: str
    password: str
    role: Role

class UserUpdate(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None
    role: Optional[Role] = None

class UserResponse(BaseModel):
    id: int
    email: str
    role: Role

    class Config:
        from_attributes = True