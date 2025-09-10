from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from typing import List
from uuid import UUID
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate

# Create a new product
async def create_product(db: AsyncSession, product_data: ProductCreate, user_id: UUID):
    new_product = Product(**product_data.dict(), user_id=user_id)
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product

# Get a product by ID
async def get_product(db: AsyncSession, product_id: UUID) -> Product | None:
    result = await db.execute(select(Product).where(Product.id == product_id))
    return result.scalar_one_or_none()

# Get all products
async def get_products(db: AsyncSession) -> List[Product]:
    result = await db.execute(select(Product))
    return result.scalars().all()

# Update a product
async def update_product(db: AsyncSession, product_id: UUID, product_update: ProductUpdate) -> Product | None:
    existing_product = await get_product(db, product_id)
    if not existing_product:
        return None
    for field, value in product_update.dict(exclude_unset=True).items():
        setattr(existing_product, field, value)
    db.add(existing_product)
    await db.commit()
    await db.refresh(existing_product)
    return existing_product

# Delete a product
async def delete_product(db: AsyncSession, product_id: UUID) -> bool:
    existing_product = await get_product(db, product_id)
    if not existing_product:
        return False
    await db.delete(existing_product)
    await db.commit()
    return True
