from pydantic import BaseModel
from app.models.user import Role

class UserCreate(BaseModel):
    email: str
    password: str
    role: Role

class UserResponse(BaseModel):
    id: int
    email: str
    role: Role

    class Config:
        from_attributes = True