item=input("What would you like to buy?: ")
price=float(input(f"What is the price of {item} ?:  "))
quantity=int(input("how many do you want?: "))
bill=price*quantity
print(f"Your total bill of {quantity} x {item}  is ${bill}")