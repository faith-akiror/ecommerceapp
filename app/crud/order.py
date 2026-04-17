from sqlalchemy.orm import Session
from app.models.order import Order, OrderStatus
from app.crud.base import CRUD


class CRUDOrder(CRUD):

    def get_by_user(self, db: Session, user_id: int):
        return db.query(Order).filter(Order.user_id == user_id).all()

    def update_status(self, db: Session, order: Order, status: str):
        allowed = {
            "pending": ["paid"],
            "paid": ["shipped"],
            "shipped": ["delivered"]
        }

        if status not in allowed.get(order.status.value, []):
            raise Exception("Invalid status transition")

        order.status = OrderStatus(status)
        db.commit()
        db.refresh(order)
        return order


order_crud = CRUDOrder(Order)