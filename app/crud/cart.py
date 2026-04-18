from sqlalchemy import func
from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.crud.base import CRUD # Import the base CRUD class

class CartCRUD(CRUD): # Inherit from CRUD
    def __init__(self, model):
        super().__init__(model)

    def create(self, db, user_id: int):
        # Check if a cart already exists for the user (though router should handle this)
        existing_cart = db.query(Cart).filter(Cart.user_id == user_id).first()
        if existing_cart:
            return existing_cart # Return existing cart if found
        
        cart_obj = Cart(user_id=user_id)
        db.add(cart_obj)
        db.commit()
        db.refresh(cart_obj)
        return cart_obj

    def add(self, db, cart_id: int, product_id: int, qty: int):
        cart_item = db.query(CartItem).filter_by(cart_id=cart_id, product_id=product_id).first()
        if cart_item:
            cart_item.quantity += qty # Update quantity if item already exists
        else:
            cart_item = CartItem(cart_id=cart_id, product_id=product_id, quantity=qty)
            db.add(cart_item)
        db.commit()
        db.refresh(cart_item)
        return cart_item

    def items(self, db, cart_id: int):
        return db.query(CartItem).filter_by(cart_id=cart_id).all()

cart = CartCRUD(Cart) # Instantiate with the Cart model