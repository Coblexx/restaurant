from enum import Enum
from pydantic import BaseModel
from .storage import *

# l_dishes = get_dishes_storage()

class DishCreateSchema(BaseModel):
    name: str
    price: float

    class Config:
        schema_extra = {
            "example": {
                "name": "Spaghetti",
                "price": 13.0
            }
        }

# OrderCreateSchema = Enum('OrderCreateScema', l_dishes)

class Dish(DishCreateSchema):
    id: int

# class Order(OrderCreateSchema):
#     id: int