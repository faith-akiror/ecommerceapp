from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.dependencies import get_db, get_current_user
from app.crud.cart import cart
from app.schemas.cart import CartResponse
from app.schemas.cart_item import CartItemCreate, CartItemResponse
from app.models.user import User

router = APIRouter()

# This endpoint might not be strictly necessary if a cart is auto-created on first item add
# or if a user always has a cart. Keeping it for explicit creation if needed.
@router.post("/", response_model=CartResponse, status_code=status.HTTP_201_CREATED)
def create_user_cart(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    if user.cart: # If user already has a cart, return it instead of creating a new one
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already has an active cart")
    return cart.create(db, user.id) # This will create a cart and associate it with the user

@router.post("/add", response_model=CartItemResponse, status_code=status.HTTP_200_OK)
def add_item_to_cart(item_in: CartItemCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    # Ensure the user has a cart, create one if not
    user_cart = user.cart
    if not user_cart:
        user_cart = cart.create(db, user.id)

    # Add or update item in the cart
    return cart.add(db, user_cart.id, item_in.product_id, item_in.quantity)

@router.get("/", response_model=List[CartItemResponse], status_code=status.HTTP_200_OK)
def get_cart_items(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    if not user.cart:
        return [] # Return empty list if user has no cart
    return cart.items(db, user.cart.id)