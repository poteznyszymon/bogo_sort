import random 

def bogo_sort(numbers):
    number_of_shuffles = 0
    original_numbers = numbers
    sorted_numbers = sorted(original_numbers)
    
    while original_numbers != sorted_numbers:
        random.shuffle(original_numbers)
        number_of_shuffles += 1
    
    return number_of_shuffles

n = 6
min_number = 1
max_number = 10
numbers = [random.randint(min_number, max_number) for _ in range(n)]

print(bogo_sort(numbers))

