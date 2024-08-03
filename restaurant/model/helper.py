import datetime


class State:
    waiting_to_select_item = 'Waiting to select item'
    waiting_to_payment = 'Waiting to payment'
    waiting_to_confirmation = 'Waiting to confirmation'
    confirm_and_finish = 'Successfully confirm and finish'
    failed = 'Failed'
    successful = 'Successful'


class DeliveryType:
    bike_delivery = 'Bike delivery'
    eat_in_restaurant = 'In restaurant'
    eat_out = 'Eat out'


class TypePay:
    online = 'Online'
    cash = 'Cash'
    transfer = 'Transfer'


character_for_discount_code = ['?', '!', '$', '#', '.']


class Role:
    super_admin = 'super_admin'
    admin = 'admin'
    customer = 'customer'

