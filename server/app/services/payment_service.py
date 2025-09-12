from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.payment import Payment
from app.schemas.payment import PaymentCreate
from uuid import UUID

async def create_payment(db: AsyncSession, payment_data: PaymentCreate) -> Payment:
    payment = Payment(
        order_id=payment_data.order_id,
        amount=payment_data.amount,
        method=payment_data.method.value,
        status="pending"
    )
    db.add(payment)
    await db.commit()
    await db.refresh(payment)
    return payment

async def get_payment(db: AsyncSession, payment_id: UUID) -> Payment | None:
    result = await db.execute(select(Payment).where(Payment.id == payment_id))
    return result.scalars().first()

async def update_payment_status(db: AsyncSession, payment_id: UUID, status: str, transaction_id: str | None = None) -> Payment | None:
    payment = await get_payment(db, payment_id)
    if not payment:
        return None
    payment.status = status
    if transaction_id:
        payment.transaction_id = transaction_id
    await db.commit()
    await db.refresh(payment)
    return payment
