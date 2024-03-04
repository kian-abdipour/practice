from sqlalchemy import Column, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship, column_property
from restaurant.model.mixin import DateTimeMixin
from restaurant.database import Base, Session
from restaurant.model.discount import Discount


class DiscountHistory(DateTimeMixin, Base):
    __tablename__ = 'discount_history'
    id = Column(Integer, primary_key=True)
    discount_id = Column(ForeignKey('discount.id'))
    payment_id = Column(ForeignKey('payment.id'))
    base_amount = Column(Float)
    affected_amount = Column(Float)
    discounted_amount = column_property(base_amount - affected_amount)  # Column property

    @classmethod
    def add(cls, discount_id, payment_id, base_amount, affected_amount):
        discount_history = cls(discount_id=discount_id, payment_id=payment_id,
                               base_amount=base_amount, affected_amount=affected_amount)
        with Session() as session:
            session.add(discount_history)
            session.query(Discount).filter(Discount.id == discount_id).update({Discount.usage_limitation:
                                                                              (Discount.usage_limitation - 1)})

            session.commit()
