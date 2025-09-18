# ============================================
# Shopping Cart Program (Tuple Version)
# ============================================

foods = ()
prices = ()
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: Rs. "))
        foods += (food,)        # create a new tuple with the new item
        prices += (price,)      # create a new tuple with the new price

# Display cart
print("\n----- YOUR CART -----")
for i in range(len(foods)):
    print(f"{foods[i]} - Rs.{prices[i]}")
    total += prices[i]

print(f"\nYour total bill: Rs.{total}")
