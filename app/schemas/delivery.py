from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.delivery import DeliveryStatus

class DeliveryAssign(BaseModel):
    order_id: int
    courier_id: int

class DeliveryStatusUpdate(BaseModel):
    status: DeliveryStatus

class DeliveryResponse(BaseModel):
    id: int
    order_id: int
    courier_id: Optional[int] = None
    status: DeliveryStatus
    created_at: datetime
    updated_at: datetime
    class Config:
        from_attributes = True