from sqlalchemy import Column, ForeignKey, Integer, Float
from sqlalchemy.orm import column_property, Session, relationship

from restaurant.model.mixin import DateTimeMixin
from restaurant.model.payment import Payment
from restaurant.model.base import Base


class DiscountHistory(DateTimeMixin, Base):
    __tablename__ = 'discount_history'
    id = Column(Integer, primary_key=True)
    discount_id = Column(ForeignKey('discount.id'))
    payment_id = Column(ForeignKey('payment.id'))
    base_amount = Column(Float)
    affected_amount = Column(Float)
    discounted_amount = column_property(base_amount - affected_amount)  # Column property

    discount = relationship('Discount', back_populates='discount_histories')

    @classmethod
    def add(cls, session: Session, discount_id, payment_id, base_amount, affected_amount):
        discount_history = cls(discount_id=discount_id, payment_id=payment_id,
                               base_amount=base_amount, affected_amount=affected_amount)

        session.add(discount_history)
        #session.query(Discount).filter(Discount.id == discount_id).update({Discount.usage_limitation:
        #                                                                  (Discount.usage_limitation - 1)})

        session.commit()

        return discount_history

    @classmethod
    def check_one_use(cls, session: Session, customer_id):
        discount_history = session.query(Payment).join(cls).filter(Payment.customer_id == customer_id).one_or_none()

        return discount_history

