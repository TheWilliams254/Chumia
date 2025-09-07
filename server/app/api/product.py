from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from uuid import UUID
from app.schemas.product import ProductCreate, ProductUpdate, ProductOut
from app.services.product_service import create_product, get_product, get_products, update_product, delete_product
from app.db import get_db

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
async def create_new_product(product: ProductCreate, db: AsyncSession = Depends(get_db)):
    return await create_product(db, product)

@router.get("/", response_model=List[ProductOut])
async def list_all_products(db: AsyncSession = Depends(get_db)):
    return await get_products(db)

@router.get("/{product_id}", response_model=ProductOut)
async def get_single_product(product_id: UUID, db: AsyncSession = Depends(get_db)):
    product = await get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=ProductOut)
async def update_existing_product(product_id: UUID, product_update: ProductUpdate, db: AsyncSession = Depends(get_db)):
    updated_product = await update_product(db, product_id, product_update)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_existing_product(product_id: UUID, db: AsyncSession = Depends(get_db)):
    success = await delete_product(db, product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return None
