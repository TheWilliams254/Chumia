import uuid
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, Float, Integer, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID
from app.db import Base
import enum

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
