import random

def get_numbers_ticket(min, max, quantity):
    return random.sample(range(min, max), quantity)

numbers_1 = get_numbers_ticket(1, 49, 6)
numbers_2 = get_numbers_ticket(1, 36, 5)
print(numbers_1)
print(numbers_2)