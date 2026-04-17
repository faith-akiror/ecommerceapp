from pydantic import BaseModel

class CartItemCreate(BaseModel):
    product_id: int
    quantity: int

class CartResponse(BaseModel):
    id: int
    user_id: int

    class Config:
        from_attributes = True