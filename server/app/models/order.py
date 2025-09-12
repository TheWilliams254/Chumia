from __future__ import annotations
from uuid import uuid4, UUID
from typing import List, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy import ForeignKey, Integer, Float, String, Enum
from app.db import Base
import enum


if TYPE_CHECKING:
    from app.models.user import User
    from app.models.product import Product
    from app.models.payment import Payment

class ItemStatus(enum.Enum):
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[UUID] = mapped_column(pgUUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(pgUUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
    status: Mapped[ItemStatus] = mapped_column(
    Enum(ItemStatus, name="order_status"),
    default=ItemStatus.PENDING,
    nullable=False
    )
    total_amount: Mapped[float] = mapped_column(Float, default=0.0)

    user: Mapped["User"] = relationship("User", back_populates="orders")
    items: Mapped[List["OrderItem"]] = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")


class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[UUID] = mapped_column(pgUUID(as_uuid=True), primary_key=True, default=uuid4)
    order_id: Mapped[UUID] = mapped_column(pgUUID(as_uuid=True), ForeignKey("orders.id", ondelete="CASCADE"))
    product_id: Mapped[UUID] = mapped_column(pgUUID(as_uuid=True), ForeignKey("products.id", ondelete="CASCADE"))
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)  # snapshot of product price at time of order

    order: Mapped["Order"] = relationship("Order", back_populates="items")
    product: Mapped["Product"] = relationship("Product", back_populates="order_items")
    payments: Mapped[list["Payment"]] = relationship("Payment", back_populates="order", cascade="all, delete-orphan")

    def __repr__(self):
        return f"OrderItem(id={self.id}, order_id={self.order_id}, product_id={self.product_id}, quantity={self.quantity}, price={self.price})"