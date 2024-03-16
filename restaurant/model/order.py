from sqlalchemy import Unicode, Column, Integer, ForeignKey
from restaurant.model.base import Base
from sqlalchemy.orm import relationship
from restaurant.model.mixin import DateTimeMixin
from restaurant.model.helper import State, DeliveryType
from restaurant.database import Session
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

    items = relationship('OrderItem', cascade='all, delete')
    payments = relationship('Payment', cascade='all, delete')

    @classmethod
    def add(cls, customer_id, address_id):
        state = State.waiting_to_confirmation

        try:
            print(f'Enter a number if your are at home you should choose bike delivery,'
                  f'\n1.{DeliveryType.bike_delivery}'
                  f'\n2.{DeliveryType.eat_in_restaurant}'
                  f'\n3.{DeliveryType.eat_out}')
            number_delivery_type = int(input(': '))
            delivery_types = [DeliveryType.bike_delivery, DeliveryType.eat_in_restaurant, DeliveryType.eat_out]
            delivery_type = delivery_types[number_delivery_type - 1]

        except ValueError:
            return print('ValueError: You should type just number')

        except IndexError:
            return print('IndexError: Number not found')

        if delivery_type == DeliveryType.eat_in_restaurant:
            condition_desk_number = True
            while condition_desk_number:
                try:
                    print('Enter your desk number')
                    desk_number = int(input(': '))

                except ValueError:
                    print('ValueError: Your desk number must be just number, try again')
                    desk_number = None

                if desk_number is not None:
                    condition_desk_number = False

        else:
            desk_number = None

        print('If you want description enter it else type No')
        description = input(': ')
        if description == '' or description == 'no' or description == 'No':
            description = None

        order = cls(state=state, delivery_type=delivery_type,
                    desk_number=desk_number, description=description,
                    address_id=address_id, customer_id=customer_id)
        with Session() as session:
            session.add(order)

            session.commit()
            session.refresh(order)

        print('Your orders successfully added please do pay and wait until admin to confirm it')
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
    def show_all_waiting_to_confirm(cls):
        with Session() as session:
            result = session.query(cls, Address.address, Payment).filter(cls.state == State.waiting_to_confirmation).join(Address).join(Payment).order_by(cls.id).all()  # Question where to be cut

        if len(result) > 0:
            for row in result:
                text_address = row[1]
                order = row[0]
                payment = row[2]
                print(f'Created at: {order.created_at}, id: {order.id}, customer_id: {order.customer_id}'
                      f' state: {order.state}, payment state: {payment.state}, address: {text_address}')

        else:
            print('Now we don\'t have any order')

    @classmethod
    def confirm(cls):
        print('Enter id of order that you want to confirm')
        try:
            order_id = int(input(': '))

        except ValueError:
            print('ValueError: You should type just number')
            order_id = None

        if order_id is not None:
            with Session() as session:
                result = session.query(cls).filter(cls.id == order_id).update(
                    {cls.state: State.confirm_and_finish}
                )

                session.commit()

            if result == 1:
                print('Order successfully confirm')

            else:
                print('Waring: Order id not found try again')

