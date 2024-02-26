from sqlalchemy import Column, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship, column_property
from restaurant.model.mixin import DateTimeMixin
from restaurant.database import Base


class DiscountHistory(DateTimeMixin, Base):
    __tablename__ = 'discount_history'
    id = Column(Integer, primary_key=True)
    discount_id = ForeignKey('discount.id')
    payment_id = ForeignKey('payment.id')
    base_amount = Column(Float)
    affected_amount = Column(Float)
    discounted_amount = column_property(base_amount - affected_amount)  # Column property

