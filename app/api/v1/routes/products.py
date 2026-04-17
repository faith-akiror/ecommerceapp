from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.dependencies import get_db, require_role
from app.crud.product import product_crud
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse

router = APIRouter()

# VENDOR CREATES PRODUCTS
@router.post("/", response_model=ProductResponse, dependencies=[Depends(require_role("vendor"))])
def create_product(product_in: ProductCreate, db: Session = Depends(get_db)):
    # Note: In a real app, you'd extract vendor_id from the current user
    return product_crud.create(db, product_in.model_dump())

# PUBLIC
@router.get("/", response_model=List[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return product_crud.get_all(db)

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return product_crud.get(db, product_id)

# VENDOR UPDATE
@router.put("/{product_id}", response_model=ProductResponse, dependencies=[Depends(require_role("vendor"))])
def update_product(product_id: int, product_in: ProductUpdate, db: Session = Depends(get_db)):
    product = product_crud.get(db, product_id)
    return product_crud.update(db, product, product_in.model_dump(exclude_unset=True))

# ADMIN DELETE
@router.delete("/{product_id}", dependencies=[Depends(require_role("admin"))])
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = product_crud.get(db, product_id)
    return product_crud.delete(db, product)