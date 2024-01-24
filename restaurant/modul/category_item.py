from sqlalchemy import Column, Integer, ForeignKey
from restaurant.modul.base import Base
from sqlalchemy.orm import relationship
from restaurant.modul.mixin import DateTimeMixin
from restaurant.modul import Category
from restaurant.modul.custom_exception import LengthError
from restaurant.database_package import Session


class CategoryItem(DateTimeMixin, Base):
    __tablename__ = 'category_item'
    id = Column(Integer, primary_key=True)
    category_id = Column(ForeignKey('category.id'))
    item_id = Column(ForeignKey('item.id'))

    categories = relationship('Category', overlaps='items', cascade='all, delete')
    items = relationship('Item', overlaps='categories', cascade='all, delete')

    @staticmethod
    def match_row(item_id):
        print('Enter name of categories of this item one enter a category name and another one again enter and'
              ' if it\'s finish type q')
        Category.show_category()
        proceed = True
        while proceed:
            name_of_category = input(': ')
            condition_mathing_row = False
            try:
                if len(name_of_category) > 40:
                    error = LengthError(massage='LengthError: Len of Name is out of 30!, try again')
                    raise error

            except LengthError:
                error.show_massage()

            with Session() as session:
                result = session.query(Category).filter(Category.name == name_of_category).one_or_none()

            if result is not None:
                category_id = result.id
                category_item = CategoryItem(category_id=category_id, item_id=item_id)
                with Session() as session:
                    session.add(category_item)

                    session.commit()

                condition_mathing_row = True
                print(f'Item successfully added to {result.name}')

            else:
                print('Category not found')

            if name_of_category == 'Q' or name_of_category == 'q':
                proceed = False

        return condition_mathing_row

