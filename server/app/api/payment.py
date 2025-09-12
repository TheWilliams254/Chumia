from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from app.db import get_db
from app.schemas.payment import PaymentCreate, PaymentOut
from app.services.payment_service import create_payment, get_payment, update_payment_status

router = APIRouter(prefix="/payments", tags=["Payments"])

@router.post("/", response_model=PaymentOut, status_code=status.HTTP_201_CREATED)
async def make_payment(payment: PaymentCreate, db: AsyncSession = Depends(get_db)):
    return await create_payment(db, payment)

@router.get("/{payment_id}", response_model=PaymentOut)
async def get_single_payment(payment_id: UUID, db: AsyncSession = Depends(get_db)):
    payment = await get_payment(db, payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@router.put("/{payment_id}/status", response_model=PaymentOut)
async def update_payment(payment_id: UUID, status: str, transaction_id: str | None = None, db: AsyncSession = Depends(get_db)):
    updated = await update_payment_status(db, payment_id, status, transaction_id)
    if not updated:
        raise HTTPException(status_code=404, detail="Payment not found")
    return updated
