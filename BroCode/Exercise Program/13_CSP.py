# ============================================
# Concession Stand Program
# ============================================

menu = {
    "popcorn": 50,
    "soda": 30,
    "coke": 30,
    "burger": 50,
    "pizza": 100,
    "caramel popcorn": 70,
    "pastry": 50,
    "fries": 40
}

cart = []
total = 0
# Show Menu
print("--------------Menu--------------")
for i, j in menu.items():
    print(f"{i}: Rs.{j}")
print("--------------------------------")

# Take Orders
while True:
    food = input("Select an item (q for quit): ").lower()  # fixed .lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        qty = int(input(f"Enter quantity of {food}: "))  # added quantity
        cart.append((food, qty))  # store tuple (item, qty)
    else:
        print("❌ Item not in menu")

# Print Receipt
print("--------------Your Order--------------")
for i, qty in cart:
    total += menu.get(i) * qty
    print(f"{i} x{qty} = Rs.{menu.get(i) * qty}")

print("--------------------------------------")
print(f"Your total bill: Rs.{total}")
