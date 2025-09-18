# ============================
# 🧮 Simple Python Weight Converter
# ============================

# ⌨️ Input
a = float(input("Enter your weight: "))
unit = input("Enter Unit? (K for Kilograms, L for Pounds): ")

# 🔁 Conversion
if unit.upper() == "K":
    print(f"Result: {a * 2.205:.2f} lbs")  # Kg to lbs
elif unit.upper() == "L":
    print(f"Result: {a / 2.205:.2f} kg")   # lbs to kg
else:
    print("❌ Invalid unit!")
