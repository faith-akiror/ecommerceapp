from pydantic import BaseModel

class OrderResponse(BaseModel):
    id: int
    user_id: int
    total: float
    status: str

    class Config:
        from_attributes = True