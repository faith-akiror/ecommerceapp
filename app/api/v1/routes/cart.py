from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db, get_current_user
from app.crud.cart import cart

router = APIRouter()

@router.post("/")
def create_cart(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return cart.create(db, user.id)

@router.post("/add")
def add_item(product_id: int, quantity: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    c = cart.create(db, user.id)
    return cart.add(db, c.id, product_id, quantity)

@router.get("/")
def get_items(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return cart.items(db, user.id)