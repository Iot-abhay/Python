# ============================================
# 📘 Python Arithmetic & Math Library Notes
# ============================================

# ▶️ Basic arithmetic operations using assignment operators
# ▶️ Built-in math functions: round(), abs(), pow(), max(), min()
# ▶️ math module: advanced math like sqrt(), ceil(), floor()

# -------------------------------
# 🧮 Arithmetic Assignment Operators
# -------------------------------

add      = 0
add     += 1          # add = add + 1

minus    = 0
minus   -= 3          # minus = minus - 3

multiply = 3
multiply*= 0          # multiply = multiply * 0

divide   = 4
divide  /= 4          # divide = divide / 4

rem      = 3
rem     %= 2          # rem = rem % 2

exp      = 5
exp    **= 2          # exp = exp ** 2

print("Arithmetic Assignment Results:")
print(f"Add: {add}, Minus: {minus}, Multiply: {multiply}, Divide: {divide}, Remainder: {rem}, Exponent: {exp}")
print()

# -------------------------------
# 🧮 Built-in Math Functions
# -------------------------------
x = 1.34
y = -5
z = 7

res1 = round(x)       # Rounds to nearest integer
res2 = abs(y)         # Absolute value
res3 = pow(z, 2)      # z to the power of 2
res4 = max(x, y, z)   # Maximum value
res5 = min(x, y, z)   # Minimum value

print("Built-in Math Function Results:")
print(f"round({x}) = {res1}")
print(f"abs({y}) = {res2}")
print(f"pow({z}, 2) = {res3}")
print(f"max(x, y, z) = {res4}")
print(f"min(x, y, z) = {res5}")
print()

# -------------------------------
# 📚 Math Module Functions
# -------------------------------
import math

print("Math Library Constants:")
print(f"Pi  = {math.pi}")
print(f"e   = {math.e}")
print()

# Math functions
result1 = math.sqrt(149)      # Square root
result2 = math.ceil(14.6)     # Rounds up
result3 = math.floor(14.6)    # Rounds down

print("Math Library Function Results:")
print(f"sqrt(149) = {result1}")
print(f"ceil(14.6) = {result2}")
print(f"floor(14.6) = {result3}")
