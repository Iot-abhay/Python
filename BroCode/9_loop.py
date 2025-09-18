# ================================================================================
# 🔤 While Loop Examples
# ================================================================================

# 1️⃣ Ask for name until user enters something
name = input("Enter your name: ")

while name == '':
    print("Did you not enter your name!")
    name = input("Enter your name: ")

print(f"Welcome {name}\n")

# ------------------------------------------------------------------------

# 2️⃣ Ask for favorite food until user types 'q'
food = input("Enter food you like (q to quit): ")
temp = food  # Store the first food for farewell message

while food != 'q':
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")

print(f"Bye {temp} lover\n")

# ------------------------------------------------------------------------

# 3️⃣ Ask for number between 1 and 10 until valid
n = int(input("Enter a number between 1 - 10: "))

while n < 1 or n > 10:
    print(f"{n} is not valid!")
    n = int(input("Enter a number between 1 - 10: "))

print(f"Your number is {n}")

# ================================================================================
# 🔄 For Loop Examples
# ================================================================================

# 1️⃣ Print numbers from 1 to n
n = int(input('Enter value of n: '))
for i in range(1, n + 1):
    print(i)

# ------------------------------------------------------------------------

# 2️⃣ Countdown from n to 1
n = int(input('Enter value of n: '))
for i in reversed(range(1, n + 1)):
    print(i)
print('HAPPY NEW YEAR')

# ------------------------------------------------------------------------

# 3️⃣ Print odd numbers from 1 to n
n = int(input('Enter value of n: '))
for i in range(1, n + 1, 2):
    print(i)

# ------------------------------------------------------------------------

# 4️⃣ Print each letter in the alphabet string
alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
    print(letter)

# ================================================================================
# Nested Loop 
# ================================================================================

#----------------------------------------------------------------------------

# Right-angled triangle pattern

# Step 1: Take input for number of rows
n = int(input("Enter value of n: "))

# Step 2: Outer loop controls the number of rows (0 to n)
for i in range(n + 1):

    # Step 3: Inner loop controls how many stars are printed in each row
    # In row i, we print (i + 1) stars
    for j in range(i + 1):
        print("*", end="")  # 'end=""' prevents moving to a new line after each star

    # Step 4: Move to the next line after printing all stars in the current row
    print()


