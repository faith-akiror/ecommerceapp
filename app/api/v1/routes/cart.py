from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db, get_current_user
from app.crud.cart import cart
from app.schemas.cart import CartResponse, CartItemCreate

router = APIRouter()

@router.post("/", response_model=CartResponse)
def create_cart(db: Session = Depends(get_db), user=Depends(get_current_user)):
    if user.cart:
        return user.cart
    return cart.create(db, user.id)

@router.post("/add")
def add_item(item_in: CartItemCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    c = user.cart if user.cart else cart.create(db, user.id)
    return cart.add(db, c.id, item_in.product_id, item_in.quantity)

@router.get("/")
def get_items(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return cart.items(db, user.cart.id) if user.cart else []