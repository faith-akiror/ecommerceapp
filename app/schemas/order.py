from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.order import OrderStatus

class OrderCreate(BaseModel):
    # Assuming order creation is triggered by a cart checkout,
    # so user_id and total might be derived, but for a direct create,
    # we might need these or a list of product_ids/quantities.
    # For simplicity, let's assume it's created internally from cart.
    pass

class OrderResponse(BaseModel):
    id: int
    user_id: int
    total: float
    status: OrderStatus
    created_at: datetime

    class Config:
        from_attributes = True