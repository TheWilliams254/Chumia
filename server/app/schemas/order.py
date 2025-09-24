from enum import Enum
from uuid import UUID
from typing import List
from pydantic import BaseModel, conint, confloat
from datetime import datetime

class ItemStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"

class OrderItemCreate(BaseModel):
    product_id: UUID
    quantity: conint(gt=1) #must be greater than 1

class OrderItemOut(BaseModel):
    id: UUID
    product_id: UUID
    quantity: confloat(gt=0)
    price: float

    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    items: List[OrderItemCreate]
    notes: str | None = None

class OrderOut(BaseModel):
    id: UUID
    user_id: UUID
    status: ItemStatus
    total_amount: float
    items: List[OrderItemOut]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class OrderStatusUpdate(BaseModel):
    status: ItemStatus
