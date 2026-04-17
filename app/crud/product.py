from sqlalchemy.orm import Session
from app.models.product import Product
from app.crud.base import CRUD


class CRUDProduct(CRUD):
    def get_by_vendor(self, db: Session, vendor_id: int):
        return db.query(Product).filter(Product.vendor_id == vendor_id).all()


product_crud = CRUDProduct(Product)