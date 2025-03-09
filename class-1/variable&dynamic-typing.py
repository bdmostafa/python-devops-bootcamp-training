# Integer variable
number = 10

# Float variable
pi = 3.14

# String variable
greeting = "Welcome to DevOps Bootcamp!"

# Boolean variable
is_valid = True

# Immutable data
a = 100
print("a =", a, " | Type:", type(a), " | id:", id(a))
a = a + 50  # allocate new memory for storing new value
print("Updated a =", a, " | id:", id(a))

# Mutable data
lst = [1, 2, 3]
print("lst =", lst, " | id:", id(lst))
lst.append(4)  # change value in the same space
print("Updated lst =", lst, " | id:", id(lst))



