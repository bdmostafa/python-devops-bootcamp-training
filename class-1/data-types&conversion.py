# Integer
age = 25

# Float
price = 19.99

# string (text)
name = "DevOps Bootcamp"

# boolean
is_active = True

# list
fruits = ["apple", "banana", "cherry"]

# Tupple - (immutable)
dimensions = (1920, 1080)

# Dictionary
student = {"name": "Rahim", "age": 22}

# Set
unique_numbers = {1, 2, 3, 4}


# type convertion 
num_str = "123"
num_int = int(num_str)      # convertion from string to integer
print("integer number", num_str + 10)  # 133

float_str = "3.14"
num_float = float(float_str)  # convertion from string to float
print("float value:", num_float)

# input function
# example for taking input from user
user_name = input("Put your name, please: ")
print("Hello", user_name, "! Welcome to DevOps Bootcamp.")

print("data type:", type(user_name))
print("data id:", id(age))


# Nested dictionary and list example
students = {
    "A101": {
        "name": "Rahim",
        "scores": [85, 90, 78],
        "details": {"age": 20, "dept": "CSE"}
    },
    "A102": {
        "name": "Karim",
        "scores": [88, 76, 95],
        "details": {"age": 21, "dept": "ECE"}
    }
}

# Getting every student name and average score
for sid, info in students.items():
    avg_score = sum(info["scores"]) / len(info["scores"])
    print(f"ID: {sid}, Name: {info['name']}, Average Score: {avg_score:.1f}")


# Value will be the square of it itself if it is even, otherwise copy it's value if odd
squares_or_identity = {i: (i**2 if i % 2 == 0 else i) for i in range(1, 11)}
print("Corrected dictionary:", squares_or_identity)


# Conversion with string/list
data = [1, 2, 3, 4, 5]
# list to string conversion with comma separated
data_str = ", ".join(str(num) for num in data)
print("string output:", data_str)

# string to list conversion
data_list = [int(x.strip()) for x in data_str.split(",")]
print("again data list:", data_list)

# try-except block usage
user_input = "123abc"
try:
    number = int(user_input)
except ValueError:
    print(f"error: '{user_input}' It's not a valid integer!")
