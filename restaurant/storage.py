from functools import lru_cache
from .schema import Dish

# OrderStorageType = dict[int, list[Order]]
# L_ORDERS: OrderStorageType = {}

# @lru_cache()
# def get_order_storage():
#     return L_ORDERS

DishStorageType = dict[int, Dish]

L_DISHES: DishStorageType = {}

@lru_cache()
def get_dishes_storage():
    return L_DISHES
