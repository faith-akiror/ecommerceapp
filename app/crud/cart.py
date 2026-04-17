from app.models.cart import Cart
from app.models.cart_item import CartItem

class CartCRUD:
    def create(self,db,user_id):
        c=Cart(user_id=user_id)
        db.add(c); db.commit(); db.refresh(c)
        return c

    def add(self,db,cart_id,product_id,qty):
        i=CartItem(cart_id=cart_id,product_id=product_id,quantity=qty)
        db.add(i); db.commit(); db.refresh(i)
        return i

    def items(self,db,cart_id):
        return db.query(CartItem).filter_by(cart_id=cart_id).all()

cart=CartCRUD()