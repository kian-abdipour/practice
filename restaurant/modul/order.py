from sqlalchemy import Unicode, Column, Integer, ForeignKey
from restaurant.modul.base import Base
from sqlalchemy.orm import relationship
from restaurant.modul.mixin import DateTimeMixin


class Order(DateTimeMixin, Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    state = Column(Unicode, nullable=False)
    delivery_type = Column(Unicode, nullable=False)
    desk_number = Column(Integer, nullable=True)
    description = Column(Unicode, nullable=True)
    address_id = Column(ForeignKey('address.id'))
    customer_id = Column(ForeignKey('customer.id'))

    items = relationship('OrderItem', cascade='all, delete')
    payments = relationship('Payment', cascade='all, delete')

