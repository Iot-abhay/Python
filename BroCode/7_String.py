# ====================================
# 🔤 String Methods in Python
# ====================================

# ⌨️ Input from user
name = input("Enter your name: ")
s = input("Enter any string: ")

# 📏 Basic Properties
length = len(name)  # Length of the string
first_a = name.find("a")  # First occurrence of 'a'
last_a = name.rfind("a")  # Last occurrence of 'a' (-1 if not found)

# 🔠 Case Conversions
capitalized = name.capitalize()  # First letter capitalized
upper = name.upper()             # Full uppercase
lower = upper.lower()            # Full lowercase (from upper)

# ✅ Validations
only_digits = name.isdigit()     # Only digits?
only_alpha = name.isalpha()      # Only alphabets?
alnum = name.isalnum()           # Alphanumeric?

# 🔁 String Modifications
a_count = s.count("a")           # Count of 'a'
a_replaced = s.replace("a", "A") # Replace 'a' with 'A'

# 📤 Output
print("\n📌 String Analysis:")
print(f"Length of name         : {length}")
print(f"First occurrence of 'a': {first_a}")
print(f"Last occurrence of 'a' : {last_a}")

print("\n🔡 Case Operations:")
print(f"Capitalized            : {capitalized}")
print(f"Uppercase              : {upper}")
print(f"Lowercase              : {lower}")

print("\n✅ Validations:")
print(f"Only Digits            : {only_digits}")
print(f"Only Alphabets         : {only_alpha}")
print(f"Alphanumeric           : {alnum}")

print("\n🔁 Transformations:")
print(f"Count of 'a' in string : {a_count}")
print(f"Replaced string        : {a_replaced}")

# ❗ Optional: Show all methods (can be commented out)
# print("\n📚 All String Methods:")
# help(str)


# ====================================
# 🔤 String Methods in Python
# ====================================

# ⌨️ Input from user
name = input("Enter your name: ")
s = input("Enter any string: ")

# 📏 Basic Properties
length = len(name)  # Length of the string
first_a = name.find("a")  # First occurrence of 'a'
last_a = name.rfind("a")  # Last occurrence of 'a' (-1 if not found)

# 🔠 Case Conversions
capitalized = name.capitalize()  # First letter capitalized
upper = name.upper()             # Full uppercase
lower = upper.lower()            # Full lowercase (from upper)

# ✅ Validations
only_digits = name.isdigit()     # Only digits?
only_alpha = name.isalpha()      # Only alphabets?
alnum = name.isalnum()           # Alphanumeric?

# 🔁 String Modifications
a_count = s.count("a")           # Count of 'a'
a_replaced = s.replace("a", "A") # Replace 'a' with 'A'

# 📤 Output
print("\n📌 String Analysis:")
print(f"Length of name         : {length}")
print(f"First occurrence of 'a': {first_a}")
print(f"Last occurrence of 'a' : {last_a}")

print("\n🔡 Case Operations:")
print(f"Capitalized            : {capitalized}")
print(f"Uppercase              : {upper}")
print(f"Lowercase              : {lower}")

print("\n✅ Validations:")
print(f"Only Digits            : {only_digits}")
print(f"Only Alphabets         : {only_alpha}")
print(f"Alphanumeric           : {alnum}")

print("\n🔁 Transformations:")
print(f"Count of 'a' in string : {a_count}")
print(f"Replaced string        : {a_replaced}")

# ❗ Optional: Show all methods (can be commented out)
# print("\n📚 All String Methods:")
# help(str)


#======================================
#Index accessing = [start: end: step]
#======================================

t=input('enter string: ')
print(t[4])
print(t[:4])
print(t[5:8])
print(t[4:])
print(t[-3])
print(t[::2])