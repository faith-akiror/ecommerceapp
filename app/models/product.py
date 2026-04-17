from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)

    vendor_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # relationships
    vendor = relationship("User", back_populates="products")
    cart_items = relationship("CartItem", back_populates="product")

    def __repr__(self):
        return f"<Product {self.name}>"