import random

def get_numbers_ticket(min:int, max:int, quantity:int) -> int:
    list_of_numbers = []
    if max - min > quantity:         
        list_of_numbers = random.sample(range(min, max), quantity)
        return sorted(list_of_numbers)
    if max - min < quantity or max < min:         
        return list_of_numbers 
    
print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(1, 36, 5))
print(get_numbers_ticket(10, 4, 2))
print(get_numbers_ticket(10, 15, 9))
print(get_numbers_ticket(-10, 5, 20))

#-- Не знаю, як правильно, це другий варіант --

import random

def get_numbers_ticket(min:int, max:int, quantity:int) -> int:
    list_of_numbers = []
    if not max - min < quantity:    
        if max - min > quantity:         
            list_of_numbers = random.sample(range(min, max), quantity)
            return sorted(list_of_numbers)
    else:        
        return list_of_numbers 
    
print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(1, 36, 5))
print(get_numbers_ticket(10, 4, 2))
print(get_numbers_ticket(10, 15, 9))
print(get_numbers_ticket(-10, 5, 20))
