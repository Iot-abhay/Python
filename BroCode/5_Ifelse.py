# ====================================
# 🔐 Age Eligibility Check with Ternary
# ====================================

# ⌨️ Standard age input and check
age = int(input("Enter your age: "))

if age >= 18 and age <= 60:
    print("✅ You are signed up!")
elif age < 0:
    print("❌ You haven't been born yet!")
elif age > 60:
    print("⚠️ You are too old to sign up!")
else:
    print("🔒 You must be 18+ to sign up!")

# ------------------------------------
# 🧪 Ternary Operator for quick check
# ------------------------------------
a = int(input("Enter your age again: "))
print("✅ You are signed up!" if a >= 18 else "🔒 You must be 18+ to sign up!")
