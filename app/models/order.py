from sqlalchemy import Column, Integer, Float, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from app.db.base import Base


class OrderStatus(str, enum.Enum):
    pending = "pending"
    paid = "paid"
    shipped = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    total = Column(Float, default=0)
    status = Column(Enum(OrderStatus), default=OrderStatus.pending)

    created_at = Column(DateTime, default=datetime.utcnow)

    # relationships
    user = relationship("User", back_populates="orders")
    delivery = relationship("Delivery", back_populates="order", uselist=False)

    def __repr__(self):
        return f"<Order {self.id} status={self.status}>"