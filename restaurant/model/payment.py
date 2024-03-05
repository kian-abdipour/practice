import datetime

from sqlalchemy import Column, Integer, Unicode, ForeignKey, Float
from restaurant.model.base import Base
from restaurant.model.mixin import DateTimeMixin
from restaurant.model.helper import State, TypePay
from sqlalchemy.orm import relationship
from restaurant.database import Session
from restaurant.model.discount import Discount
from restaurant.model.discount_history import DiscountHistory
from copy import deepcopy


class Payment(DateTimeMixin, Base):
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True)
    state = Column(Unicode, nullable=False)
    type = Column(Unicode, nullable=False)
    amount = Column(Float, nullable=False)
    order_id = Column(ForeignKey('order.id'))
    customer_id = Column(ForeignKey('customer.id'))

    discount_histories = relationship('DiscountHistory', cascade='all, delete')

    @classmethod
    def add(cls, list_item, order_id, customer_id):
        state = State.failed
        type_pay = TypePay.transfer
        amount = 0
        for item in list_item:
            amount += item.price
            print(f'name: {item.name}, price: {item.price}')

        # Process of apply discount
        proceed_apply_discount = True
        while proceed_apply_discount:
            print(f'Your total amount is {amount} if you have discount code '
                  f'and you want to use it type it\'s code else, type No')
            discount_code = input(': ')
            if discount_code != 'no' and discount_code != 'No' and discount_code != '':
                discount = Discount.search_by_code(discount_code)
                if discount is not None:
                    condition_discount_disposable = cls.check_discount_disposable(customer_id, discount.id)

                    # This part is to check we pass the start date of our discount of not
                    condition_start_date = False
                    if discount.start_date is not None:
                        if discount.start_date < datetime.datetime.utcnow().date():
                            condition_start_date = True

                    else:
                        condition_start_date = True

                    # This part is to check the expiry date of our discount
                    condition_expire_date = False
                    if discount.expire_date is not None:
                        if datetime.datetime.utcnow().date() < discount.expire_date:
                            condition_expire_date = True

                    else:
                        condition_start_date = True

                    if discount.usage_limitation != 0:
                        if condition_start_date:
                            if condition_expire_date:
                                if condition_discount_disposable:
                                    discounted_amount = amount * (discount.percent / 100)
                                    affected_amount = amount - discounted_amount
                                    base_amount = deepcopy(amount)
                                    amount = affected_amount
                                    proceed_apply_discount = False

                                else:
                                    print(f'Waring: You use this discount before')

                            else:
                                print(f'The expire date of this discount is {discount.expire_date} and we passed it')

                        else:
                            print(f'This discount can be use after {discount.start_date}')

                    else:
                        print('Usage limitation of this discount is finished')

                else:
                    print('Discount code not found')

            else:
                discount_code = None
                proceed_apply_discount = False

        # Process of payment after apply discount
        print(f'Your total amount after discount is {amount} if you want to pay type yes, else type no')
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

            result = session.query(cls).filter(cls.created_at == payment.created_at).one()

        if discount_code is not None:
            if discount is not None and condition_expire_date and condition_start_date and condition_discount_disposable:
                DiscountHistory.add(discount.id, result.id, base_amount, affected_amount)

        if state == State.failed:  # Ask question about why payment.state raise a sqlalchemy Error ?
            return False

        elif state == State.successful:
            return True

    @classmethod
    def check_discount_disposable(cls, customer_id, discount_id):
        with Session() as session:
            result = session.query(DiscountHistory).filter(cls.customer_id == customer_id,
                                                           DiscountHistory.discount_id == discount_id).one_or_none()

        if result is None:
            return True

        else:
            return False

