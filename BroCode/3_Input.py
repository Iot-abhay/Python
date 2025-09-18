# ==========================================
# 📘 Python User Input & Basic Calculations
# ==========================================

# ▶️ input(...) → Takes input from user
# ▶️ Always returns a string, must convert if needed (int, float, etc.)

# -------------------------------
# 🧾 User Info + Birthday Bill
# -------------------------------
name = input("What is your name, sir?: ")
age = input("How old are you?: ")
age = int(age) + 1

guests = float(input("How many people will you invite?: "))
bill = guests * 500

print(f"\nHello {name} 👋")
print("Happy Birthday! 🎉")
print(f"Here is your bill: ₹{bill} for your {age}th birthday celebration.\n")

