from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime
import enum

class ItemsCategory(str, enum.Enum):
    doors = "doors"
    windows = "windows"
    metal_furniture = "metal furniture"
    cookers = "cookers"
    curtain_materials = "curtain materials"
    decoration = "decoration"

# Shared fields
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    category: ItemsCategory
    image_url: Optional[str] = None

# For creating new products
class ProductCreate(ProductBase):
    pass

# For updating existing products
class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    category: Optional[ItemsCategory] = None
    image_url: Optional[str] = None

# For output / responses
class ProductOut(ProductBase):
    id: UUID
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
