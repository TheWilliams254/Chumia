from uuid import UUID
from pydantic import BaseModel
from typing import Optional
from enum import Enum

class PaymentMethod(str, Enum):
    mpesa = "mpesa"
    card = "card"
    paypal = "paypal"

class PaymentStatus(str, Enum):
    pending = "pending"
    success = "success"
    failed = "failed"

class PaymentCreate(BaseModel):
    order_id: UUID
    amount: float
    method: PaymentMethod

class PaymentOut(BaseModel):
    id: UUID
    order_id: UUID
    amount: float
    method: PaymentMethod
    status: PaymentStatus
    transaction_id: Optional[str]

    class Config:
        orm_mode = True
