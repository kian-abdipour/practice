from sqlalchemy import Column, DateTime
from datetime import datetime


class DateTimeMixin:
    created_at = Column(DateTime, default=datetime.utcnow)


class State:
    waiting_to_select_item = 'Waiting to select_item'
    waiting_to_payment = 'Waiting to payment'
    waiting_to_confirmation = 'Waiting to confirmation'
    confirm_and_finish = 'Successfully confirm and finish'


class DeliveryType:
    bike_delivery = 'Bike delivery'
    eat_in_restaurant = 'In restaurant'
    eat_out = 'Outside'

