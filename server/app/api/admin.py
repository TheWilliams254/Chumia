# app/api/admin.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from uuid import UUID

from app.db import get_db
from app.models.user import User
from app.schemas.user import UserOut as UserSchema
from app.core.security import get_current_user as get_admin_user
router = APIRouter(prefix="/api/admin", tags=["Admin"])

@router.get("/users", response_model=List[UserSchema])
async def list_all_users(
    db: AsyncSession = Depends(get_db),
    admin_user: User = Depends(get_admin_user)
):
    """
    Admin-only: Get all users in the system.
    """
    result = await db.execute(select(User))
    return result.scalars().all()


@router.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(
    user_id: UUID,
    db: AsyncSession = Depends(get_db),
    admin_user: User = Depends(get_admin_user)
):
    """
    Admin-only: Delete a specific user by ID.
    """
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    await db.delete(user)
    await db.commit()
    return {"detail": f"User {user_id} deleted successfully"}