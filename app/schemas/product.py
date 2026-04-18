from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    price: float
    stock: int

class ProductCreate(ProductBase):
    # vendor_id should not be provided by the client, it's set by the server based on current user
    pass 

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    # vendor_id should not be updatable by the client

class ProductResponse(ProductBase):
    id: int
    vendor_id: int

    class Config:
        from_attributes = True