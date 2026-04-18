from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.dependencies import get_db, require_role, get_current_user
from app.crud.delivery import delivery_crud
from app.models.user import User
from app.schemas.delivery import DeliveryAssign, DeliveryStatusUpdate, DeliveryResponse

router = APIRouter()

# ADMIN assigns courier
@router.post("/assign", response_model=DeliveryResponse, status_code=status.HTTP_201_CREATED)
def assign_delivery(
    delivery_in: DeliveryAssign,
    db: Session = Depends(get_db),
    admin_user: User = Depends(require_role("admin"))
):
    # You might want to add checks here if the order_id and courier_id are valid
    return delivery_crud.assign(db, delivery_in.order_id, delivery_in.courier_id)

# COURIER views own deliveries
@router.get("/", response_model=List[DeliveryResponse], status_code=status.HTTP_200_OK)
def get_my_deliveries(db: Session = Depends(get_db), courier: User = Depends(require_role("courier"))):
    # 'courier' is already the User object from require_role
    return delivery_crud.get_by_courier(db, courier.id)

# COURIER updates status
@router.put("/{delivery_id}", response_model=DeliveryResponse, status_code=status.HTTP_200_OK)
def update_delivery_status(
    delivery_id: int,
    status_update: DeliveryStatusUpdate,
    db: Session = Depends(get_db),
    current_courier: User = Depends(require_role("courier"))
):
    delivery = delivery_crud.get(db, delivery_id)
    if not delivery or delivery.courier_id != current_courier.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Delivery not found or not authorized")
    return delivery_crud.update_status(db, delivery, status_update.status)