# Arithmetic opreator

a = 15
b = 4

print("Addition:", a + b)            
print("Subtraction:", a - b)         
print("Multiplication:", a * b)
print("Division:", a / b)           # float output
print("Floor Division:", a // b)    # Floor Division
print("Modulas:", a % b)            # Remainder
print("Exponentiation:", a ** b)



# Relational operator
# Returns boolean value
print("a > b:", a > b)   #is greatet than?
print("a == b:", a == b) # is equal?
print("a != b:", a != b) # is not equal?



# Logical operator
# Returns boolean value
x = True
y = False
print("x and y:", x and y)  # returns true if both side is true
print("x or y:", x or y)    # returns true if anyone is true
print("not x:", not x)      # returns opposite always



numbers = [-10, -5, 0, 5, 10, 15]

# List comprehension and filter usage
positive_numbers = [num for num in numbers if num > 0]
total = sum(positive_numbers)
print("positive number:", positive_numbers)
print("summation of positive numbers:", total)


# Bitwise operator
x = 0b1100  # 12 in decimal
y = 0b1010  # 10 in decimal

print("x & y =", bin(x & y))  # বিটওয়াইজ AND
print("x | y =", bin(x | y))  # বিটওয়াইজ OR
print("x ^ y =", bin(x ^ y))  # বিটওয়াইজ XOR
print("~x =", bin(~x))        # বিটওয়াইজ NOT
