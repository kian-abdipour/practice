from fastapi import APIRouter, HTTPException, status, Depends, Header

from restaurant.scheme.category_item import CategoryItemForRead, AdditionItemToCategory, DeleteItemFromCategory
from restaurant.database import get_session
from restaurant.model import Category, CategoryItem, Item
from restaurant.authentication import check_token
from restaurant.model.helper import Role

from sqlalchemy.orm import Session

from typing import Annotated

router = APIRouter(
    prefix='/category_items',
    tags=['category_item']
)


