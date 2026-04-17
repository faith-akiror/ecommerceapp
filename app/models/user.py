from sqlalchemy import Column, Integer, String, Enum
from app.core.database import Base
import enum

class Role(str, enum.Enum):
    admin = "admin"
    vendor = "vendor"
    courier = "courier"
    customer = "customer"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(Enum(Role), default=Role.customer)