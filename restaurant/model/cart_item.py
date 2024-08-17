from sqlalchemy import Column, Integer, Float, ForeignKey, Column
from sqlalchemy.orm import relationship, Session, column_property, query

from restaurant.model.base import Base
from restaurant.model.mixin import DateTimeMixin
from restaurant.model.item import Item
from restaurant.database import get_session
from restaurant.custom_exception import OutOfStockError, ItemNotInCartError

from copy import deepcopy

for database_session in get_session():
    db_session = database_session


class CartItem(DateTimeMixin, Base):
    __tablename__ = 'cart_item'
    id = Column(Integer, primary_key=True)
    item_id = Column(ForeignKey('item.id'))
    cart_id = Column(ForeignKey('cart.id'))
    quantity = Column(Integer, default=1, nullable=False)
    unit_amount = column_property(db_session.query(Item.price).filter(Item.id == item_id))
    total_amount = column_property(unit_amount * quantity)

    cart = relationship('Cart', overlaps='items', cascade='all, delete', back_populates='items')
    item = relationship('Item', overlaps='carts', cascade='all, delete', back_populates='carts')

    @classmethod
    def add(cls, session: Session, item_id, cart_id, quantity):
#        if cart_item_in_database is not None:
#            session.query(cls).filter(cls.id == cart_item_in_database.id).update({cls.quantity: cls.quantity + quantity})
#
#            session.commit()
#            session.refresh(cart_item_in_database)
#
#            return cart_item_in_database

        cart_item = cls(item_id=item_id, cart_id=cart_id, quantity=quantity)

        session.add(cart_item)

        session.commit()
        session.refresh(cart_item)

        return cart_item

    @classmethod
    def delete(cls, session: Session, item_id, cart_id):
        cart_item = cls.search_by_item_id(session=session, item_id=item_id, cart_id=cart_id)
        if cart_item is None:
            return None

        cart_item_for_response = deepcopy(cart_item)
        session.query(cls).filter(cls.item_id == item_id, cls.cart_id == cart_id).delete()

        session.commit()

        return cart_item_for_response

    @classmethod
    def update_quantity(cls, session: Session, item_id, cart_id, quantity, item):
        cart_item_in_database = cls.search_by_item_id(session=session, item_id=item_id, cart_id=cart_id)
        if cart_item_in_database is None:
            if quantity == 1:
                if item.stock == 0:
                    raise OutOfStockError('')

                cart_item = cls(cart_id=cart_id, item_id=item_id, quantity=quantity)
                session.add(cart_item)

                session.commit()

                return cart_item

            else:
                raise ItemNotInCartError('')

        if cart_item_in_database.quantity == 1 and quantity == -1:
            session.query(cls).filter(cls.id == cart_item_in_database.id).delete()

            session.commit()

            return cart_item_in_database

        if cart_item_in_database.quantity >= item.stock:
            raise OutOfStockError('')

        session.query(cls).filter(cls.item_id == item_id, cls.cart_id == cart_id).update(
            {cls.quantity: cls.quantity + quantity}
        )
        session.refresh(cart_item_in_database)

        session.commit()

        return cart_item_in_database

    @classmethod
    def search_by_item_id(cls, session: Session, item_id, cart_id):
        cart_item = session.query(cls).filter(cls.item_id == item_id, cls.cart_id == cart_id).one_or_none()

        return cart_item

    @classmethod
    def search_by_cart_id(cls, session: Session, cart_id, cart_item_filter):
        cart_items = cart_item_filter.sort(session.query(cls).filter(cls.cart_id == cart_id)).all()

        return cart_items


