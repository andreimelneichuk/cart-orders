from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from fastapi import HTTPException
from app.models import Product, Order, OrderItem

async def get_product(db, product_id: int):
    result = await db.execute(select(Product).where(Product.id == product_id))
    return result.scalar_one_or_none()

async def create_order(db, order_data):
    order = Order(status=order_data.status)
    for item_data in order_data.items:
        product = await get_product(db, item_data.product_id)
        if product and product.stock >= item_data.quantity:
            product.stock -= item_data.quantity
            order.items.append(OrderItem(product_id=item_data.product_id, quantity=item_data.quantity))
        else:
            raise HTTPException(status_code=400, detail="Insufficient stock")
    db.add(order)
    await db.commit()
    return order