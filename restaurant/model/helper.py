import random
import string


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
    eat_out = 'Outside'


class TypePay:
    online = 'Online'
    cash = 'Cash'
    transfer = 'Transfer'


character_for_discount_code = ['?', '!', '$', '#', '.']

# This process is for making code of our discount
code = ''
while len(code) != 3:
    code = code + random.choice(string.ascii_letters)

while len(code) != 6:
    code = code + random.choice(string.digits)

code = code + str(ord(random.choice(string.ascii_letters)))

while len(code) != 10:
    code = code + random.choice(character_for_discount_code)

print(code)