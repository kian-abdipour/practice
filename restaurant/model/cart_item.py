from sqlalchemy import Column, Integer, Float, ForeignKey, Column
from sqlalchemy.orm import relationship, Session, column_property, query

from restaurant.model.base import Base
from restaurant.model.mixin import DateTimeMixin
from restaurant.model.item import Item
#from restaurant.session import get_session


#for database_session in get_session():
#    session = database_session


class CartItem(DateTimeMixin, Base):
    __tablename__ = 'cart_item'
    id = Column(Integer, primary_key=True)
    item_id = Column(ForeignKey('item.id'))
    cart_id = Column(ForeignKey('cart.id'))
    quantity = Column(Integer, default=1, nullable=False)
    unit_amount = Column(Integer) #column_property(Item.search_by_id(session=session, item_id=item_id).price)
    total_amount = Column(Integer) #column_property(unit_amount * quantity)

    cart = relationship('Cart', overlaps='items', cascade='all, delete', back_populates='items')
    item = relationship('Item', overlaps='carts', cascade='all, delete', back_populates='carts')

    @classmethod
    def add(cls, session: Session, item_id, cart_id, quantity):
        cart_item = cls(item_id=item_id, cart_id=cart_id, quantity=quantity)

        session.add(cart_item)

        session.commit()
        session.refresh(cart_item)

        return cart_item

    @classmethod
    def delete(cls, session: Session, item_id, cart_id):
        cart_item = session.query(cls).filter(cls.item_id == item_id, cls.cart_id == cart_id).one_or_none()
        if cart_item is None:
            return None

        session.query(cls).filter(cls.item_id == item_id, cls.cart_id == cart_id).delete()

        session.commit()

        return cart_item

    @classmethod
    def decrease_quantity(cls, session: Session, item_id, cart_id):
        cart_item = session.query(cls).filter(cls.item_id == item_id, cls.cart_id == cart_id).one_or_none()
        if cart_item is None:
            return None

        if cart_item.quantity == 1:
            cls.delete(session=session, item_id=item_id, cart_id=cart_id)

        session.query(cls).filter(cls.item_id == item_id, cls.cart_id == cart_id).update(
            {cls.quantity: cls.quantity - 1}
        )

        return cart_item

