from sqlalchemy import Unicode, Column, Integer, ForeignKey
from restaurant.modul.base import Base
from sqlalchemy.orm import relationship
from restaurant.modul.mixin import DateTimeMixin, State, DeliveryType
from restaurant.database_package import Session


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

    @staticmethod
    def add(customer_id, address_id):
        state = State.waiting_to_confirmation

        try:
            print(f'Enter a number'
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
            desk_number = input('')

        else:
            desk_number = None

        print('If you want description enter it else type No')
        description = input('')
        if description == '' or description == 'no' or description == 'No':
            description = None

        order = Order(state=state, delivery_type=delivery_type,
                      desk_number=desk_number, description=description,
                      address_id=address_id, customer_id=customer_id)
        with Session() as session:
            session.add(order)

            session.commit()

        print('Your orders successfully added please wait until admin to confirm it')

