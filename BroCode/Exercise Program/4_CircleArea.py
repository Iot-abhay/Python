# =====================================================
# 📘 Geometry Calculations: Circle & Right-Angled Triangle
# =====================================================

import math

# =======================================
# ⚪ Circle Geometry: Area & Circumference
# =======================================

# ▶️ Formula:
#     Circumference = 2 × π × r
#     Area          = π × r²

# -------------------------------
# ⌨️ Input: Radius
# -------------------------------
r = float(input("Enter the radius of the circle (in meters): "))

# -------------------------------
# 🔁 Calculations
# -------------------------------
circumference = 2 * math.pi * r
area = math.pi * (r ** 2)

# -------------------------------
# 📤 Output
# -------------------------------
print(f"\n🔵 Circle:")
print(f"Circumference: {round(circumference, 2)} meters")
print(f"Area        : {round(area, 2)} square meters")

# =======================================
# 📐 Right-Angled Triangle: Hypotenuse
# =======================================

# ▶️ Formula:
#     hypotenuse = √(a² + b²)

# -------------------------------
# ⌨️ Input: Sides A and B
# -------------------------------
a = float(input("\nEnter side A of the triangle (in meters): "))
b = float(input("Enter side B of the triangle (in meters): "))

# -------------------------------
# 🔁 Calculation
# -------------------------------
hypotenuse = math.sqrt(a ** 2 + b ** 2)

# -------------------------------
# 📤 Output
# -------------------------------
print(f"Hypotenuse (side C): {round(hypotenuse, 2)} meters")
