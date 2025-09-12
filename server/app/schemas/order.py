from enum import Enum
from uuid import UUID
from typing import List
from pydantic import BaseModel

class ItemStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"

class OrderItemCreate(BaseModel):
    product_id: UUID
    quantity: int

class OrderItemOut(BaseModel):
    id: UUID
    product_id: UUID
    quantity: int
    price: float

    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    items: List[OrderItemCreate]

class OrderOut(BaseModel):
    id: UUID
    user_id: UUID
    status: ItemStatus
    total_amount: float
    items: List[OrderItemOut]

    class Config:
        orm_mode = True

class OrderStatusUpdate(BaseModel):
    status: ItemStatus
