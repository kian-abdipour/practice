from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship, Session, ColumnProperty

from restaurant.model.base import Base
from restaurant.model.mixin import DateTimeMixin
from restaurant.model.item import Item
from restaurant.custom_exception import OutOfStockError

from copy import deepcopy


class OrderItem(DateTimeMixin, Base):
    __tablename__ = 'order_item'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, default=1, nullable=False)
    unit_amount = Column(Float, nullable=False)
    total_amount = ColumnProperty(unit_amount*quantity)
    order_id = Column(ForeignKey('order.id'))
    item_id = Column(ForeignKey('item.id'))

    order = relationship('Order', overlaps='items', cascade='all, delete', back_populates='items')
    item = relationship('Item', overlaps='orders', cascade='all, delete', back_populates='orders')

    @classmethod
    def add(cls, session: Session, order_id, item_id, quantity, unit_amount, total_amount):
        order_item = cls(
            quantity=quantity, unit_amount=unit_amount,
            total_amount=total_amount, order_id=order_id, item_id=item_id
        )
        item = session.query(Item).filter(Item.id == item_id).one()
        if item.stock == 0:
            raise OutOfStockError(massage='The item is out of stock')

        session.add(order_item)
        session.query(Item).filter(Item.id == item_id).update({Item.stock: (Item.stock - quantity)})

        session.commit()
        session.refresh(order_item)

        return order_item

