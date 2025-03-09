# lambda function
double = lambda x: x * 2
print("Double of 5:", double(5))

# Getting square value
square = lambda x: x ** 2
print(square(5))  # Output: 25




# lambda func vs general func ===================
def add(a, b):
    return a + b

print(add(5, 10))  # Output: 15

add = lambda a, b: a + b
print(add(5, 10))  # Output: 15




# Getting double value of every elements of the list using map()
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print("doubled list:", doubled_numbers) # Output: doubled list: [2, 4, 6, 8, 10]

# Getting only odd number using filter()
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("odd numbers:", odd_numbers) #Output: odd numbers: [1, 3, 5]




# Getting max value between 2 numbers
maximum = lambda a, b: a if a > b else b
print(maximum(15, 30))  # Output: 30




# Sorting with Lambda
names = ["Rahim", "Karim", "Joya", "Samiha"]
names_sorted = sorted(names, key=lambda name: len(name))  
print(names_sorted)  # Output: ['Joya', 'Rahim', 'Karim', 'Samiha']




# Have to import functools module for using reduce() 
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15




# List Comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Dictionary Comprehension
numbers = [1, 2, 3, 4, 5]
squared_dict = {x: x ** 2 for x in numbers}
print(squared_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}




# Higher Order Functions (HOF)
def apply_function(func, value):
    return func(value)

square = lambda x: x ** 2
result = apply_function(square, 5)
print(result)  # Output: 25





# Example -> Log filtering through functional programming
logs = [
    "INFO: Server started",
    "ERROR: Database connection failed",
    "WARNING: High memory usage detected",
    "ERROR: Disk full",
]

error_logs = list(filter(lambda log: "ERROR" in log, logs))
print(error_logs)
# Output: ['ERROR: Database connection failed', 'ERROR: Disk full']
