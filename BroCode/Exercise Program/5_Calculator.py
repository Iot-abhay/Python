# ============================
# 🧮 Simple Python Calculator
# ============================

# ⌨️ Input
a = float(input("Enter value of a: "))
op = input("Enter operator (+ - * /): ")
b = float(input("Enter value of b: "))

# 🔁 Calculation using if-elif-else
if op == "+":
    print(f"Result: {a + b}")
elif op == "-":
    print(f"Result: {a - b}")
elif op == "*":
    print(f"Result: {a * b}")
elif op == "/":
    if b != 0:
        print(f"Result: {a / b}")
    else:
        print("❌ Cannot divide by zero!")
else:
    print("❌ Invalid operator!")
