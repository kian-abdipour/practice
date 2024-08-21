from sqlalchemy import Unicode, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, Session

from restaurant.model.base import Base
from restaurant.model.mixin import DateTimeMixin
from restaurant.model.helper import State, DeliveryType


class Order(DateTimeMixin, Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    state = Column(Unicode, nullable=False)
    delivery_type = Column(Unicode, nullable=False)
    desk_number = Column(Integer, nullable=True)
    description = Column(Unicode, nullable=True)
    address_id = Column(ForeignKey('address.id'))
    customer_id = Column(ForeignKey('customer.id'))
    payment_id = Column(ForeignKey('payment.id'))

    items = relationship('OrderItem', back_populates='order')
    payments = relationship('Payment', back_populates='order')
    customer = relationship('Customer', back_populates='orders')

    @classmethod
    def add(cls, session: Session, state, delivery_type, desk_number, description, payment_id, address_id, customer_id):
        order = cls(
            state=state,
            delivery_type=delivery_type,
            desk_number=desk_number,
            description=description,
            payment_id=payment_id,
            address_id=address_id,
            customer_id=customer_id
        )
        session.add(order)

        session.commit()
        session.refresh(order)

        return order

    @classmethod
    def show_all_for_customer(cls, session: Session, customer_id, order_filter):
        result = order_filter.sort(session.query(cls).filter(cls.customer_id == customer_id)).all()

        return result

    @classmethod
    def show_by_state_for_admin(cls, session: Session, state, order_filter):
        result = order_filter.sort(session.query(cls).filter(cls.state == state)).all()

        return result

    @classmethod
    def show_by_state_for_customer(cls, session: Session, customer_id, state, order_filter):
        result = order_filter.sort(session.query(cls).filter(
            cls.state == state, cls.customer_id == customer_id
        )).all()

        return result

    @classmethod
    def search_by_id(cls, session: Session, order_id):
        order = session.query(cls).filter(cls.id == order_id).one_or_none()

        return order

    @classmethod
    def confirm(cls, session: Session, order_id):
        order = cls.search_by_id(session=session, order_id=order_id)
        if order is None:
            return None

        session.query(cls).filter(cls.id == order_id).update(
            {cls.state: State.confirm_and_finish}
        )

        session.commit()
        session.refresh(order)

        return order

    @classmethod
    def search_by_customer_id(cls, session: Session, customer_id):
        orders = session.query(cls).filter(cls.customer_id == customer_id).all()

        return orders

    @classmethod
    def show_all_for_admin(cls, session: Session, order_filter):
        orders = order_filter.sort(session.query(cls)).all()

        return orders

    @classmethod
    def search_by_customer_id_and_order_id(cls, session: Session, customer_id, order_id):
        orders = session.query(cls).filter(cls.customer_id == customer_id, cls.id == order_id).one_or_none()

        return orders

