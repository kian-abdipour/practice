from sqlalchemy import Column, Integer, Float, ForeignKey, Column
from sqlalchemy.orm import relationship, Session, column_property, query

from restaurant.model.base import Base
from restaurant.model.mixin import DateTimeMixin
from restaurant.model.item import Item
from restaurant.database import get_session

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
    def add(cls, session: Session, item_id, cart_id, quantity, cart_item_in_database):
        if cart_item_in_database is not None:
            session.query(cls).filter(cls.id == cart_item_in_database.id).update({cls.quantity: cls.quantity + quantity})

            session.commit()
            session.refresh(cart_item_in_database)

            return cart_item_in_database

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
    def decrease_quantity(cls, session: Session, item_id, cart_id):
        cart_item = cls.search_by_item_id(session=session, item_id=item_id, cart_id=cart_id)
        if cart_item is None:
            return None

        if cart_item.quantity == 1:
            cls.delete(session=session, item_id=item_id, cart_id=cart_id)

            session.commit()

            return cart_item

        session.query(cls).filter(cls.item_id == item_id, cls.cart_id == cart_id).update(
            {cls.quantity: cls.quantity - 1}
        )

        session.commit()

        return cart_item

    @classmethod
    def search_by_item_id(cls, session: Session, item_id, cart_id):
        cart_item = session.query(cls).filter(cls.item_id == item_id, cls.cart_id == cart_id).one_or_none()

        return cart_item

    @classmethod
    def search_by_cart_id(cls, session: Session, cart_id):
        cart_items = session.query(cls).filter(cls.cart_id == cart_id).all()

        return cart_items


