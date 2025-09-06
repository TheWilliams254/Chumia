from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from uuid import UUID

from app.db import get_db
from app.models.user import User
from app.schemas.user import UserOut, UserCreate
from app.schemas.responses import MessageResponse
from app.services.auth_service import register_user
from app.core.security import get_current_admin_user

router = APIRouter(prefix="/api/admin", tags=["Admin"])


@router.post("/register-admin", response_model=UserOut)
async def create_admin(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user),
):
    """
    Create a new admin.  
    First admin can be created without authentication (bootstrap).
    """
    result = await db.execute(select(User).where(User.is_admin == True))
    existing_admin = result.scalars().first()

    if not existing_admin:
        return await register_user(user_data, db, is_admin=True)

    return await register_user(user_data, db, is_admin=True)


@router.get("/users", response_model=List[UserOut])
async def get_all_users(
    db: AsyncSession = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user),
):
    """
    Admin-only: Get all registered users.
    """
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users


@router.delete("/users/{user_id}", response_model=MessageResponse)
async def delete_user(
    user_id: UUID,
    db: AsyncSession = Depends(get_db),
    admin_user: User = Depends(get_current_admin_user),
):
    """
    Admin-only: Delete a specific user by ID.
    """
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Prevent self-deletion
    if user.id == admin_user.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Admins cannot delete their own account"
        )

    await db.delete(user)
    await db.commit()
    return {"detail": f"User '{user.username}' ({user.email}) deleted successfully"}
