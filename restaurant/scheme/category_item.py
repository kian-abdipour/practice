from pydantic import BaseModel
from restaurant.scheme.item import ItemForRead
from restaurant.scheme.category import CategoryForRead

from typing import List


class CategoryItemForRead(CategoryForRead):
    id: int
    name: str
    items: List[ItemForRead]

    class Config:
        from_attributes = True


class AdditionItemToCategory(BaseModel):
    item_id: int
    category_id: int

    class Config:
        from_attributes = True


class DeleteItemFromCategory(AdditionItemToCategory):
    pass

