from sqlalchemy import Unicode, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, Session

from restaurant.model.base import Base
from restaurant.model.mixin import DateTimeMixin
from restaurant.model.helper import State, DeliveryType
from restaurant.model.address import Address
from restaurant.model.payment import Payment


class Order(DateTimeMixin, Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    state = Column(Unicode, nullable=False)
    delivery_type = Column(Unicode, nullable=False)
    desk_number = Column(Integer, nullable=True)
    description = Column(Unicode, nullable=True)
    address_id = Column(ForeignKey('address.id'))
    customer_id = Column(ForeignKey('customer.id'))

    items = relationship('OrderItem', cascade='all, delete', back_populates='order')
    payments = relationship('Payment', cascade='all, delete', back_populates='order')
    customer = relationship('Customer', back_populates='orders')

    @classmethod
    def add(cls, session: Session, state, delivery_type, desk_number, description, address_id, customer_id):
        order = cls(
            state=state,
            delivery_type=delivery_type,
            desk_number=desk_number,
            description=description,
            address_id=address_id,
            customer_id=customer_id
        )
        session.add(order)

        session.commit()
        session.refresh(order)

        return order

    @classmethod
    def show_all_for_customer(cls, customer_id):
        with Session() as session:
            result = session.query(cls, Address.address).filter(cls.customer_id == customer_id).join(Address).order_by(cls.id).all()

        if len(result) > 0:
            for row in result:
                text_address = row[1]
                order = row[0]
                print(f'Created at: {order.created_at}, id: {order.id}, state: {order.state}, address: {text_address}')

        else:
            print('History of your order is empty')

    @classmethod
    def show_all_waiting_to_confirm(cls, session: Session):
        result = session.query(cls, Address.address, Payment).filter(cls.state == State.waiting_to_confirmation).join(Address).join(Payment).order_by(cls.id).all()  # Question where to be cut

        #if len(result) > 0:
        #    for row in result:
        #        text_address = row[1]
        #        order = row[0]
        #        payment = row[2]
        #        print(f'Created at: {order.created_at}, id: {order.id}, customer_id: {order.customer_id}'
        #              f' state: {order.state}, payment state: {payment.state}, address: {text_address}')
#
        #else:
        #    print('Now we don\'t have any order')

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

