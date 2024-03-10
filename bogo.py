import random
import matplotlib.pyplot as plt


def bogo_sort(numbers):
    number_of_shuffles = 0
    original_numbers = numbers.copy()
    sorted_numbers = sorted(original_numbers)
    
    while original_numbers != sorted_numbers:
        random.shuffle(original_numbers)
        number_of_shuffles += 1
    
    return number_of_shuffles


n = 6
min_number = 1
max_number = 10
numbers = [random.randint(min_number, max_number) for _ in range(n)]

#print(bogo_sort(numbers))

times_of_shuffle = []
times = 11
for i in range(times):
    times_of_shuffle.append(bogo_sort(numbers))
print(times_of_shuffle)

plt.plot(times_of_shuffle,linestyle="",marker="o")
plt.ylabel('number of shuffles')
plt.xlabel(f'number of sorting: {times}')
plt.show()
