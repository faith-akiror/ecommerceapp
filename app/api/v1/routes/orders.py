from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db, get_current_user, require_role
from app.models.order import Order, OrderStatus
from app.models.cart import Cart

router = APIRouter()


# CREATE ORDER FROM CART
@router.post("/")
def create_order(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    cart = db.query(Cart).filter(Cart.user_id == user.id).first()

    if not cart or not cart.items:
        raise HTTPException(400, "Cart is empty")

    total = sum(item.product.price * item.quantity for item in cart.items)

    order = Order(
        user_id=user.id,
        total=total,
        status=OrderStatus.pending
    )

    db.add(order)

    # clear cart
    for item in cart.items:
        db.delete(item)

    db.commit()
    db.refresh(order)

    return order


# GET USER ORDERS
@router.get("/")
def get_orders(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return db.query(Order).filter(Order.user_id == user.id).all()


# ADMIN UPDATE STATUS
@router.put("/{order_id}")
def update_status(
    order_id: int,
    status: OrderStatus,
    db: Session = Depends(get_db),
    admin=Depends(require_role("admin"))
):
    order = db.query(Order).get(order_id)

    if not order:
        raise HTTPException(404, "Order not found")

    order.status = status
    db.commit()
    db.refresh(order)

    return order