from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
import enum

from app.db.base import Base


class Role(str, enum.Enum):
    admin = "admin"
    vendor = "vendor"
    courier = "courier"
    customer = "customer"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum(Role), nullable=False)

    # relationships
    products = relationship("Product", back_populates="vendor")
    orders = relationship("Order", back_populates="user")
    cart = relationship("Cart", back_populates="user", uselist=False)
    deliveries = relationship("Delivery", foreign_keys="Delivery.courier_id")

    def __repr__(self):
        return f"<User {self.email}>"