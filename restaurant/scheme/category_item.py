from pydantic import BaseModel
from scheme.item import ItemForRead
from scheme.category import CategoryForRead

from typing import List


class CategoryItemForRead(CategoryForRead):
    items: List[ItemForRead]

    class Config:
        from_attributes = True


class AdditionItemToCategory(BaseModel):
    item_id: int

    class Config:
        from_attributes = True


class DeleteItemFromCategory(AdditionItemToCategory):
    category_id: int


class AdditionItemToCategoryForRead(DeleteItemFromCategory):
    item_id: int

    class Config:
        from_attributes = True

