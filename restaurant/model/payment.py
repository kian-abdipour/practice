from sqlalchemy import Column, Integer, Unicode, ForeignKey
from restaurant.model.base import Base
from restaurant.model.mixin import DateTimeMixin
from restaurant.model.helper import State, TypePay
from restaurant.database import Session


class Payment(DateTimeMixin, Base):
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True)
    state = Column(Unicode, nullable=False)
    type = Column(Unicode, nullable=False)
    amount = Column(Integer, nullable=False)
    order_id = Column(ForeignKey('order.id'))
    customer_id = Column(ForeignKey('customer.id'))

    @classmethod
    def add(cls, list_item, order_id, customer_id):
        state = State.failed
        type_pay = TypePay.transfer
        amount = 0
        for item in list_item:
            amount += item.price
            print(f'name: {item.name}, price: {item.price}')

        print(f'Your total amount is {amount} if you want to pay type yes, else type no')
        proceed = True
        while proceed:
            operation_pay = input(': ')
            if operation_pay == 'yes' or operation_pay == 'Yes':
                print('Pay was successful')
                state = State.successful
                proceed = False

            elif operation_pay == 'no' or operation_pay == 'No':
                print('Pay was failed')
                state = State.failed
                proceed = False

            else:
                print(f'Your total amount is {amount} if you want to pay type yes, else type no')

        payment = cls(state=state, type=type_pay, amount=amount, order_id=order_id, customer_id=customer_id)

        with Session() as session:
            session.add(payment)

            session.commit()

        if state == State.failed:  # Ask question about why payment.state raise a sqlalchemy Error ?
            return False

        elif state == State.successful:
            return True

            