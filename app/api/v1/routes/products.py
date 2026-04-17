from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db, require_role
from app.crud.product import product_crud
from app.models.product import Product

router = APIRouter()

# VENDOR CREATES PRODUCTS
@router.post("/", dependencies=[Depends(require_role("vendor"))])
def create_product(data: dict, db: Session = Depends(get_db)):
    return product_crud.create(db, data)

# PUBLIC
@router.get("/")
def get_products(db: Session = Depends(get_db)):
    return product_crud.get_all(db)

@router.get("/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    return product_crud.get(db, product_id)

# VENDOR UPDATE
@router.put("/{product_id}", dependencies=[Depends(require_role("vendor"))])
def update_product(product_id: int, data: dict, db: Session = Depends(get_db)):
    product = product_crud.get(db, product_id)
    return product_crud.update(db, product, data)

# ADMIN DELETE
@router.delete("/{product_id}", dependencies=[Depends(require_role("admin"))])
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = product_crud.get(db, product_id)
    return product_crud.delete(db, product)