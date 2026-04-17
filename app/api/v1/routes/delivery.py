from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db, require_role
from app.crud.delivery import delivery_crud

router = APIRouter()

# ADMIN assigns courier
@router.post("/assign", dependencies=[Depends(require_role("admin"))])
def assign(order_id: int, courier_id: int, db: Session = Depends(get_db)):
    return delivery_crud.assign(db, order_id, courier_id)

# COURIER views own deliveries
@router.get("/", dependencies=[Depends(require_role("courier"))])
def get_my_deliveries(db: Session = Depends(get_db), courier=Depends(require_role("courier"))):
    return delivery_crud.get_by_courier(db, courier.id)

# COURIER updates status
@router.put("/{delivery_id}", dependencies=[Depends(require_role("courier"))])
def update_status(delivery_id: int, status: str, db: Session = Depends(get_db)):
    delivery = delivery_crud.get(db, delivery_id)
    return delivery_crud.update_status(db, delivery, status)