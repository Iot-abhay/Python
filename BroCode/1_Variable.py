# 👑 Bro Code - Personal Info Display

# 👉 String Variables
Name = "Abhay Palway"
Gmail = "24io10ab2@mitsgwl.ac.in"

# ❌ Incorrect: Just prints literal text, not variables
print("Name + Gmail")

# ✅ Correct: Using f-strings to include variables
print(f"My name is: {Name}")
print(f"My Gmail is: {Gmail}")

# 👉 Integer Variable
age = 19
print(f"My age is: {age}.")

# 👉 Float Variables
sgpa1 = 8.4
sgpa2 = 8.14
cgpa = "8.27"  # keeping it as a string for display, optional

# ✅ Add space in the string where needed
print(f"My Sem 1 SGPA is {sgpa1} and Sem 2 SGPA is {sgpa2}.")
print(f"My First Year CGPA is {cgpa}.")

# 👉 Boolean

is_pass=True 
#is_pass=False
if is_pass: print("You pass bro")
else: print("You fail bro")