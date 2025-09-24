from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from uuid import UUID
from app.models.order import Order, OrderItem
from app.models.product import Product
from app.schemas.order import OrderCreate, OrderOut, OrderStatusUpdate

async def create_order(db: AsyncSession, user_id: UUID, order_data: OrderCreate):
    order = Order(user_id=user_id)
    total_amount = 0

    for item in order_data.items:
        product = await db.get(Product, item.product_id)
        if not product or product.stock < item.quantity:
            raise ValueError(f"Product {item.product_id} unavailable or insufficient stock")

        # decrease stock
        product.stock -= item.quantity

        order_item = OrderItem(
            product_id=item.product_id,
            quantity=item.quantity,
            price=product.price  # snapshot price
        )
        order.items.append(order_item)
        total_amount += product.price * item.quantity

    order.total_amount = total_amount
    db.add(order)
    await db.commit()
    await db.refresh(order)

    # reload order with items eagerly loaded
    result = await db.execute(
        select(Order).options(selectinload(Order.items)).where(Order.id == order.id)
    )
    return result.scalar_one()


async def get_order(db: AsyncSession, order_id: UUID):
    result = await db.execute(
        select(Order)
        .options(selectinload(Order.items))
        .where(Order.id == order_id)
    )
    return result.scalar_one_or_none()

async def get_user_orders(db: AsyncSession, user_id: UUID):
    result = await db.execute(
        select(Order)
        .options(selectinload(Order.items))
        .where(Order.user_id == user_id)
    )
    return result.scalars().all()

async def update_order_status(db: AsyncSession, order_id: UUID, status_update: OrderStatusUpdate):
    order = await db.get(Order, order_id)
    if not order:
        return None
    order.status = status_update.status
    await db.commit()
    await db.refresh(order)
    return order