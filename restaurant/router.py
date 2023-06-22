from fastapi import APIRouter
from .storage import get_dishes_storage
from .schema import DishCreateSchema, Dish
# from .schema import DishCreateSchema, OrderCreateSchema, Dish

router = APIRouter()

l_dishes = get_dishes_storage()
# l_orders = get_order_storage()

@router.get("/")
async def get_menu():
    return list(l_dishes.values())

@router.post("/")
async def create_dish(dish: DishCreateSchema) -> Dish:
    id = len(l_dishes) + 1

    new_dish = Dish(**dish.dict(), id=id)
    l_dishes[id] = new_dish
    return new_dish

# @router.post("/orders/{order_id}")
# async def post_order(order_id: int, order: OrderCreateSchema(dishes_storage=l_dishes)) -> None:
    
#     l_orders[order_id] = order
#     return l_orders