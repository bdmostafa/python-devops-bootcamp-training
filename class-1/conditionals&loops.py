age = 25

# if-elif-else block example
if age >= 18:
    print("You are eligible for voting")
elif age == 17:
    print("Still you are not eligible for voting")
else:
    print("You are very young!")


num = int(input("Enter a number: "))

if num > 0:
    print("This is a positive number")
elif num < 0:
    print("This is a negative number")
else:
    print("The number is zero")





# Ternary Operator
age = int(input("Enter your age: "))
status = "adult" if age >= 60 else "boy"
print("Your status:", status)





fruits = ["apple", "banana", "cherry"]

# for loop
for fruit in fruits:
    print(fruit)

# while loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1  # inreament

# for loop with range
for i in range(1, 6):  
    print(f"Current number: {i}")






# loop control - break, continue, pass
# break
for num in range(1, 10):
    if num == 5:
        print("stop looping")
        break
    print(num)


# continue
for num in range(1, 10):
    if num == 5:
        continue
    print(num)


# pass
for num in range(1, 5):
    if num == 3:
        pass  # doing nothing here
    print(num)





# Real example of loop with condition
correct_password = "Python123"
attempts = 3

for attempt in range(attempts):
    password = input("Enter password: ")
    
    if password == correct_password:
        print("Welcome! You logged in successfully!")
        break
    else:
        print(f"Wrong password! You can try {attempts - (attempt + 1)} again.")
else:
    print("Your chance has been ended. So now your account is locked.")





# List comprehension with for loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print("even numbers:", even_numbers)


# Alternative (general loop)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("even numbers:", even_numbers)


# Practical Example – Fibonacci Series Using Loop
n = int(input("Enter the length of Fibonacci series: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
 