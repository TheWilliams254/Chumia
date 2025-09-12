from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import List
from app.db import get_db
from app.schemas.order import OrderCreate, OrderOut, OrderStatusUpdate
from app.services.order_service import create_order, get_order, get_user_orders, update_order_status
from app.core.security import get_current_user, get_current_admin_user

router = APIRouter(prefix="/orders", tags=["Orders"])

# User: create new order
@router.post("/", response_model=OrderOut, status_code=status.HTTP_201_CREATED)
async def create_new_order(
    order_data: OrderCreate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):
    try:
        return await create_order(db, current_user.id, order_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# User: list own orders
@router.get("/", response_model=List[OrderOut])
async def list_my_orders(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return await get_user_orders(db, current_user.id)

# Admin: get single order
@router.get("/{order_id}", response_model=OrderOut)
async def get_single_order(
    order_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_admin=Depends(get_current_admin_user)
):
    order = await get_order(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

# Admin: update order status
@router.put("/{order_id}/status", response_model=OrderOut)
async def change_order_status(
    order_id: UUID,
    status_update: OrderStatusUpdate,
    db: AsyncSession = Depends(get_db),
    current_admin=Depends(get_current_admin_user)
):
    order = await update_order_status(db, order_id, status_update)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
