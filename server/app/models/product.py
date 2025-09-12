import uuid
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, Float, Integer, DateTime, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.db import Base
import enum
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.media import Media
    from app.models.order import OrderItem

class ItemsCategory(enum.Enum):
    doors = "doors"
    windows = "windows"
    metal_furniture = "metal furniture"
    cookers = "cookers"
    curtain_materials = "curtain materials"
    decoration = "decoration"

class Product(Base):
    __tablename__ = "products"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    stock: Mapped[int] = mapped_column(Integer, default=0)
    category: Mapped[ItemsCategory] = mapped_column(Enum(ItemsCategory, name="items_category"), nullable=False)
    image_url: Mapped[str | None] = mapped_column(String(500))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), onupdate=datetime.utcnow)

    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
    #relationships
    user: Mapped["User"] = relationship("User", back_populates="product")
    media: Mapped[List["Media"]] = relationship(back_populates="product")
    order_items: Mapped[List["OrderItem"]] = relationship("OrderItem", back_populates="product")



    def __repr__(self):
        return f"<Product {self.name}>", f"<Product {self.id}>", f"<Product {self.description}>", f"<Product {self.price}>", f"<Product {self.stock}>", f"<Product {self.category}>", f"<Product {self.image_url}>", f"<Product {self.created_at}>", f"<Product {self.updated_at}>"
