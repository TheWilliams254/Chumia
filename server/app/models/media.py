from __future__ import annotations

from uuid import UUID, uuid4
from typing import Optional, TYPE_CHECKING

from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as pgUUID

from app.db import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.product import Product


class Media(Base):
    __tablename__ = "media"

    id: Mapped[UUID] = mapped_column(pgUUID(as_uuid=True), primary_key=True, default=uuid4)
    file_url: Mapped[str] = mapped_column(String, nullable=False)
    file_type: Mapped[str] = mapped_column(String, nullable=False)

    user_id: Mapped[UUID] = mapped_column(pgUUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
    product_id: Mapped[UUID] = mapped_column(pgUUID(as_uuid=True), ForeignKey("products.id", ondelete="CASCADE"))

    user: Mapped["User"] = relationship("User", back_populates="media")
    product: Mapped["Product"] = relationship("Product", back_populates="media")