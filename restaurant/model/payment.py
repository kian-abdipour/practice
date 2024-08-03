import datetime

from sqlalchemy import Column, Integer, Unicode, ForeignKey, Float
from sqlalchemy.orm import relationship, Session

from copy import deepcopy

from restaurant.model.base import Base
from restaurant.model.mixin import DateTimeMixin
from restaurant.model.helper import State, TypePay
from restaurant.model.discount import Discount
from restaurant.model.discount_history import DiscountHistory


class Payment(DateTimeMixin, Base):
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True)
    state = Column(Unicode, nullable=False)
    type = Column(Unicode, nullable=False)
    amount = Column(Float, nullable=False)
    customer_id = Column(ForeignKey('customer.id'))

    discount_histories = relationship('DiscountHistory', cascade='all, delete')
    customer = relationship('Customer', back_populates='payments')
    order = relationship('Order', back_populates='payments')

    @classmethod
    def add(cls, session: Session, state, type_, amount, customer_id):
        payment = cls(state=state, type=type_, amount=amount, customer_id=customer_id)
        session.add(payment)

        session.commit()
        session.refresh(payment)

        return payment

#    # This method is to check that customer used a specific discount or not
#    @classmethod
#    def check_discount_disposable(cls, session: Session, customer_id, discount_id):
#        result = session.query(DiscountHistory).join(cls).filter(cls.customer_id == customer_id, DiscountHistory.discount_id == discount_id).one_or_none()3
#
#       return result

    @classmethod
    def show_all(cls, session: Session):
        payments = session.query(cls).all()

        return payments

    @classmethod
    def search_by_id(cls, session: Session, payment_id):
        payment = session.query(cls).filter(cls.id == payment_id).one_or_none()

        return payment
