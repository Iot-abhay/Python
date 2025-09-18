# ============================================
# Collections in Python
# ============================================
# A 'collection' is a single variable used to store multiple values.

# List:
#   - Syntax: []
#   - Ordered and changeable (mutable).
#   - Allows duplicate values.

# Set:
#   - Syntax: {}
#   - Unordered and unindexed.
#   - No duplicate values allowed.
#   - Mutable (can add/remove elements, but items themselves must be immutable).

# Tuple:
#   - Syntax: ()
#   - Ordered and unchangeable (immutable).
#   - Allows duplicate values.
#   - Faster than lists.

# ============================================
# Example: List
# ============================================

fruits = ["apple", "banana", "papaya", "grapes"]

# Printing the list
print(fruits)
print(fruits[3])              # Single element
print(fruits[0:2])            # Slicing
print(fruits[::2])            # Step slicing
print(fruits[::-1])           # Reverse

# Loop through list
for fruit in fruits:
    print(fruit)

print(dir(fruits))            # List methods
print(len(fruits))            # Length
print("apple" in fruits)      # Membership

fruits.append("pineapple")
fruits.remove("banana")
fruits.insert(2, "kiwi")
fruits.sort()
print(fruits)

if "kiwi" in fruits:
    print(fruits.index("kiwi"))

print(fruits.count("apple"))
fruits.clear()
print(fruits)

# ============================================
# Example: Set
# ============================================

fruits = {"apple", "banana", "papaya", "grapes", "apple"}  # Duplicate ignored

print(fruits)                  # Entire set
for fruit in fruits:
    print(fruit)

print(dir(fruits))             # Set methods
print(len(fruits))
print("apple" in fruits)

fruits.add("pineapple")        # Add element
fruits.discard("banana")       # Remove if present
fruits.pop()                   # Remove random element
print(fruits)

fruits.update({"mango", "orange"})  # Add multiple
fruits.clear()                  # Clear set
print(fruits)

# ============================================
# Example: Tuple
# ============================================

fruits = ("apple", "banana", "papaya", "grapes", "apple")

print(fruits)
print(fruits[3])
print(fruits[0:2])
print(fruits[::2])
print(fruits[::-1])

for fruit in fruits:
    print(fruit)

print(dir(fruits))             # Tuple methods (limited)
print(len(fruits))
print("apple" in fruits)

print(fruits.count("apple"))   # Count occurrences
print(fruits.index("banana"))  # Find index
# Tuples are immutable — no append, remove, insert, sort, or clear
