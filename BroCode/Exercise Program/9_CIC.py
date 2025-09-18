# ================================================================================
# 💰 Simple Compound Interest Calculator with Validation
# ================================================================================

p = 0
r = 0
t = 0

while p <= 0:
    try:
        p = float(input("Enter Principal: "))
        if p <= 0:
            print("❌ Principal can't be lower or equal to 0")
    except ValueError:
        print("❌ Please enter a valid number")
        p = 0  # reset so loop continues

while r <= 0:
    try:
        r = float(input("Enter Interest rate: "))
        if r <= 0:
            print("❌ Interest rate can't be lower or equal to 0")
    except ValueError:
        print("❌ Please enter a valid number")
        r = 0

while t <= 0:
    try:
        t = int(input("Enter Time in years: "))
        if t <= 0:
            print("❌ Time can't be lower or equal to 0")
    except ValueError:
        print("❌ Please enter a valid number")
        t = 0

# Compound Interest Formula
ci = p * pow((1+r/100), t)
print(f"Total balance after {t} year/s: ${ci:.2f}")
