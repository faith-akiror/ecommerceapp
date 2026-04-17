from sqlalchemy import Column,Integer,ForeignKey,String
from app.db.base import Base

class Delivery(Base):
    __tablename__="deliveries"
    id=Column(Integer,primary_key=True)
    order_id=Column(Integer,ForeignKey("orders.id"))
    courier_id=Column(Integer,ForeignKey("users.id"))
    status=Column(String,default="assigned")