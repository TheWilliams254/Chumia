# app/api/admin.py
from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from app.db import get_db
from app.models.user import User
from app.schemas.user import UserOut, UserCreate
from app.services.auth_service import register_user
from app.core.security import get_current_admin_user

router = APIRouter(prefix="/api/admin", tags=["Admin"])


@router.post("/register-admin", response_model=UserOut)
async def create_admin(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user),
):
    # Bootstrap condition
    result = await db.execute(select(User).where(User.is_admin == True))
    existing_admin = result.scalars().first()
    
    if not existing_admin:
        # allow first admin creation without login
        return await register_user(user_data, db, is_admin=True)

    # Otherwise require current_admin
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
