from sqlalchemy.orm import Session
from app.models.delivery import Delivery
from app.crud.base import CRUD


class CRUDDelivery(CRUD):

    def assign(self, db: Session, order_id: int, courier_id: int):
        delivery = Delivery(order_id=order_id, courier_id=courier_id)
        db.add(delivery)
        db.commit()
        db.refresh(delivery)
        return delivery

    def get_by_courier(self, db: Session, courier_id: int):
        return db.query(Delivery).filter(Delivery.courier_id == courier_id).all()

    def update_status(self, db: Session, delivery: Delivery, status: str):
        delivery.status = status
        db.commit()
        db.refresh(delivery)
        return delivery


delivery_crud = CRUDDelivery(Delivery)