from sqlalchemy import Column, Integer, ForeignKey
from restaurant.model.base import Base
from sqlalchemy.orm import relationship
from restaurant.model.mixin import DateTimeMixin
from restaurant.model import Category, Item
from restaurant.custom_exception import LengthError
from restaurant.database import Session


class CategoryItem(DateTimeMixin, Base):
    __tablename__ = 'category_item'
    id = Column(Integer, primary_key=True)
    category_id = Column(ForeignKey('category.id'))
    item_id = Column(ForeignKey('item.id'))

    categories = relationship('Category', overlaps='items', cascade='all, delete')
    items = relationship('Item', overlaps='categories', cascade='all, delete')

    @classmethod
    def match_row(cls, item_id):
        print('Enter name of categories of this item one enter a category name and another one again enter and'
              ' if it\'s finish type q')
        Category.show_all()
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
                category = session.query(Category).filter(Category.name == name_of_category).one_or_none()

            if category is not None:
                category_id = category.id
                category_item = cls(category_id=category_id, item_id=item_id)
                with Session() as session:
                    result = session.query(cls).filter(cls.category_id == category_id, cls.item_id == item_id).all()

                    if len(result) > 0:
                        return print('This item already is in this category')

                    session.add(category_item)

                    session.commit()

                condition_mathing_row = True
                print(f'Item successfully added to {category.name}')

            else:
                print('Category not found')

            if name_of_category == 'Q' or name_of_category == 'q':  # Ask question
                proceed = False

        return condition_mathing_row

    @classmethod
    def delete(cls, category_id, item_id):
        with Session() as session:
            result = session.query(cls).filter(cls.category_id == category_id, cls.item_id == item_id).delete()

            session.commit()

        if result == 1:
            print('Item successfully deleted from category')

        else:
            print('Waring: Deleting operation was fail')

    @classmethod
    def show_item_side(cls, category_id):
        with Session() as session:
            results = session.query(Item).join(cls).filter(cls.category_id == category_id).all()
            # Ask question about >>> CategoryItem.item_id == CategoryItem.item_id

        if len(results) > 0:
            for result in results:
                print(f'id: {result.id}, name: {result.name},'
                      f' country: {result.country}, price: {result.price},'
                      f' stock: {result.stock}, description: {result.description}')
            return True

        else:
            print('Now this category doesn\'t have any item')
            return False
