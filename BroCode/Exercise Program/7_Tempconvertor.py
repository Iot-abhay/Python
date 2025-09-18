# ============================
# 🌡️ Simple Python Temperature Converter
# ============================

# ⌨️ Input
a = float(input("Enter your Temperature: "))
currunit = input("Enter Current Unit? (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
unit = input("Enter Converting Unit? (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

# 🔁 Conversion Logic
result = None

if currunit == "C":
    if unit == "F":
        result = (a * 9/5) + 32
    elif unit == "K":
        result = a + 273.15
    elif unit == "C":
        result = a

elif currunit == "F":
    if unit == "C":
        result = (a - 32) * 5/9
    elif unit == "K":
        result = ((a - 32) * 5/9) + 273.15
    elif unit == "F":
        result = a

elif currunit == "K":
    if unit == "C":
        result = a - 273.15
    elif unit == "F":
        result = ((a - 273.15) * 9/5) + 32
    elif unit == "K":
        result = a

else:
    print("❌ Invalid current unit!")

# ✅ Output
if result is not None:
    print(f"Converted Temperature: {result:.2f}°{unit}")
else:
    print("❌ Invalid conversion unit!")
