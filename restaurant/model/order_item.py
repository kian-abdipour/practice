from sqlalchemy import Column, Integer, ForeignKey
from restaurant.model.base import Base
from sqlalchemy.orm import relationship
from restaurant.model.mixin import DateTimeMixin
#from restaurant.database import Session
from copy import deepcopy
from restaurant.model import Item


class OrderItem(Base, DateTimeMixin):
    __tablename__ = 'order_item'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, default=1, nullable=False)
    unit_amount = Column(Integer, nullable=False)
    total_amount = Column(Integer, default=0, nullable=False)
    order_id = Column(ForeignKey('order.id'))
    item_id = Column(ForeignKey('item.id'))

    orders = relationship('Order', overlaps='items', cascade='all, delete')
    items = relationship('Item', overlaps='orders', cascade='all, delete')

    @classmethod
    def add(cls, order_id, list_item, list_item_id):
        list_item_deep_copy = deepcopy(list_item)
        list_item_id_deep_copy = deepcopy(list_item_id)

        for item in list_item:
            item_id = item.id
            unit_amount = item.price
            quantity = list_item_id_deep_copy.count(item_id)
            total_amount = item.price * quantity
            while item.id in list_item_id_deep_copy:
                list_item_deep_copy.pop(list_item_id_deep_copy.index(item_id))
                list_item_id_deep_copy.remove(item_id)

            order_item = cls(quantity=quantity, unit_amount=unit_amount,
                             total_amount=total_amount, order_id=order_id, item_id=item_id)
            with Session() as session:
                session.add(order_item)
                session.query(Item).filter(Item.id == item.id).update({Item.stock: (Item.stock - quantity)})

                session.commit()

            if len(list_item_deep_copy) == 0:
                return

