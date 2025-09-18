# ===============================
# 📘 Python Type Checking & Conversion Notes
# ===============================

# ▶️ type(...) → Used to check data type of a variable
# ▶️ str(), int(), float(), bool() → Used for type conversion

# -------------------------------
# 🧾 Variable Definitions
# -------------------------------
name = "abhay"          # str
age = 19                # int
gpa = 8.27              # float
is_ok = True            # bool

true_str = "True"       # non-empty string (will be True in boolean)
false_str = ""          # empty string (will be False in boolean)

# -------------------------------
# 📌 Type Checking
# -------------------------------
print("=== Type Checking ===")
print(f"name       : {type(name)}")
print(f"age        : {type(age)}")
print(f"gpa        : {type(gpa)}")
print(f"is_ok      : {type(is_ok)}")
print()

# -------------------------------
# 🔁 Type Conversion Examples
# -------------------------------
print("=== Type Conversion ===")

# int to float
age = float(age)
print(f"int to float: {age} → {type(age)}")

# float to str
gpa = str(gpa)
print(f"float to string: '{gpa}' → {type(gpa)}")

# string to bool
true_bool = bool(true_str)
false_bool = bool(false_str)
print(f'string "True" to bool: {true_bool}')
print(f'string "" to bool: {false_bool}')
