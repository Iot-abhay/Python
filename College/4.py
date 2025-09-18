# # Experiment 1: Basics of Python Programming

# # Fundamental Data Types
# a = 10            # int
# b = 3.14          # float
# c = 2 + 3j        # complex
# d = True          # bool
# e = "Hello Python"  # string

# print("Values:")
# print(a, b, c, d, e)

# # Using id(), type(), range()
# print("\nData Types:")
# print("Type of a:", type(a))
# print("Type of b:", type(b))
# print("Type of c:", type(c))
# print("Type of d:", type(d))
# print("Type of e:", type(e))

# print("\nMemory IDs:")
# print("ID of a:", id(a))
# print("ID of b:", id(b))

# print("\nRange Example:")
# for i in range(1, 6):
#     print(i, end=" ")





# Experiment 2: Operators Demonstration

# x = 10
# y = 3

# # i) Arithmetic Operators
# print("Arithmetic Operators:")
# print("x + y =", x + y)
# print("x - y =", x - y)
# print("x * y =", x * y)
# print("x / y =", x / y)
# print("x % y =", x % y)
# print("x ** y =", x ** y)  # exponent
# print("x // y =", x // y)  # floor division

# # ii) Relational Operators
# print("\nRelational Operators:")
# print("x > y:", x > y)
# print("x == y:", x == y)

# # iii) Assignment Operators
# print("\nAssignment Operators:")
# z = 5
# z += 2
# print("z after z += 2:", z)

# # iv) Logical Operators
# print("\nLogical Operators:")
# print("x > 5 and y < 5:", x > 5 and y < 5)
# print("x > 5 or y > 5:", x > 5 or y > 5)
# print("not(x > y):", not(x > y))

# # v) Bitwise Operators
# print("\nBitwise Operators:")
# print("x & y:", x & y)  # AND
# print("x | y:", x | y)  # OR
# print("x ^ y:", x ^ y)  # XOR
# print("~x:", ~x)        # NOT
# print("x << 2:", x << 2)  # Left shift
# print("x >> 2:", x >> 2)  # Right shift



# Experiment 3: Input and Output Functions

# # i) input()
# name = input("Enter your name: ")

# # ii) print()
# print("Hello,", name)

# # iii) sep attribute
# print("Python", "is", "fun", sep=" - ")

# # iv) end attribute
# print("This is line 1", end=" | ")
# print("This is line 2")

# # v) String replacement operator (% formatting)
# age = 20
# print("My name is %s and I am %d years old." % (name, age))



# Experiment 4: Conditional Statements

num = int(input("Enter a number: "))

# i) if statement
if num > 0:
    print("The number is positive")

# ii) if-else statement
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

