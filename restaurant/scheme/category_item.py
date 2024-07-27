from pydantic import BaseModel
from restaurant.scheme.item import ItemForRead
from restaurant.scheme.category import CategoryForRead


class CategoryItemForRead(BaseModel, CategoryForRead):
    items: [ItemForRead]

    class Config:
        from_attributes = True


class AdditionItemToCategory(BaseModel):
    item_id: int
    category_id: int

    class Config:
        from_attributes = True


class DeleteItemFromCategory(AdditionItemToCategory):
    pass

