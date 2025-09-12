from fastapi import APIRouter, Depends, HTTPException
from app.services.mpesa_service import lipa_na_mpesa
from app.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/mpesa", tags=["M-Pesa"])

@router.post("/stkpush")
async def initiate_payment(phone_number: str, amount: float, db: AsyncSession = Depends(get_db)):
    try:
        response = lipa_na_mpesa(phone_number, amount, "ORDER123", "Order Payment")
        return {"message": "STK Push initiated", "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/callback")
async def mpesa_callback(data: dict, db: AsyncSession = Depends(get_db)):
    # Safaricom will post payment result here
    print("M-Pesa Callback:", data)
    # TODO: Update Payment + Order status in DB
    return {"ResultCode": 0, "ResultDesc": "Accepted"}
