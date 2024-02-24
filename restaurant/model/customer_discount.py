from sqlalchemy import Column, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from restaurant.database import Base
from restaurant.model.mixin import DateTimeMixin


class CustomerDiscount(DateTimeMixin, Base):
    __tablename__ = 'customer_discount'
    customer_id = ForeignKey('customer.id')
    discount_id = ForeignKey('discount.id')
#    condition_used = Column(Boolean)

    customers = relationship('Customer', overlaps='discounts', cascade='all, delete')
    discounts = relationship('Discount', overlaps='customers', cascade='all, delete')

