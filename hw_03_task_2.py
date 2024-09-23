import random

def get_numbers_ticket(min, max, quantity):
    return random.sample(range(min, max), quantity)

numbers_1 = get_numbers_ticket(1, 49, 6)
numbers_2 = get_numbers_ticket(1, 36, 5)
print(f'Six random numbers: {numbers_1}')
print(f'Five random numbers: {numbers_2}')