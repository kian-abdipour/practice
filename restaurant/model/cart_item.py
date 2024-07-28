from sqlalchemy import Column, Integer, Float, ForeignKey, Column
from sqlalchemy.orm import relationship, Session, ColumnProperty, query

from restaurant.model.base import Base
from restaurant.model.mixin import DateTimeMixin
from restaurant.model.item import Item


class CartItem(DateTimeMixin, Base):
    __tablename__ = 'cart_item'
    id = Column(Integer, primary_key=True)
    item_id = Column(ForeignKey('item.id'))
    cart_id = Column(ForeignKey('cart.id'))
    quantity = Column(Integer, default=1, nullable=False)
    unit_amount = ColumnProperty(query(Item).filter(item_id == Item.id).one().price)
    total_amount = ColumnProperty(unit_amount * quantity)

    carts = relationship('Cart', overlaps='items', cascade='all, delete')
    items = relationship('Item', overlaps='carts', cascade='all, delete')

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

