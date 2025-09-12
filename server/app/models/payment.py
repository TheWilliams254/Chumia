from __future__ import annotations
from uuid import uuid4, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy import ForeignKey, Float, String, Enum
from app.db import Base
import enum

class PaymentStatus(enum.Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"

class PaymentMethod(enum.Enum):
    MPESA = "mpesa"
    CARD = "card"
    PAYPAL = "paypal"

class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[UUID] = mapped_column(pgUUID(as_uuid=True), primary_key=True, default=uuid4)
    order_id: Mapped[UUID] = mapped_column(pgUUID(as_uuid=True), ForeignKey("orders.id", ondelete="CASCADE"))
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    method: Mapped[str] = mapped_column(String, nullable=False)  # mpesa, card, etc.
    status: Mapped[str] = mapped_column(String, default=PaymentStatus.PENDING.value)
    transaction_id: Mapped[str] = mapped_column(String, unique=True, nullable=True)

    order: Mapped["Order"] = relationship("Order", back_populates="payments")
