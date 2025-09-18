# ============================================
# 2D Collections in Python: List, Set, Tuples
# ============================================

# -------- Using LIST of LISTS --------
fruits_list = ["Apple", "Banana", "Papaya", "Grapes"]
veggies_list = ["Cabbage", "Potato", "Tomato", "Peas"]
fastfood_list = ["Momos", "Noodles", "French fries", "Manchurian"]

groceries_list = [fruits_list, veggies_list, fastfood_list]
print("\n--- LIST of LISTS ---")
print(groceries_list)
print(groceries_list[0])
print(groceries_list[2][3])

for i in groceries_list:
    for j in i:
        print(j, end=" ")
    print()


# -------- Using SET of SETS --------
# ⚠ Sets are unordered → Indexing is NOT possible
# So we can only iterate, not directly access with [index]
fruits_set = {"Apple", "Banana", "Papaya", "Grapes"}
veggies_set = {"Cabbage", "Potato", "Tomato", "Peas"}
fastfood_set = {"Momos", "Noodles", "French fries", "Manchurian"}

groceries_set = {frozenset(fruits_set), frozenset(veggies_set), frozenset(fastfood_set)}
print("\n--- SET of SETS ---")
for i in groceries_set:
    for j in i:
        print(j, end=" ")
    print()


# -------- Using TUPLE of TUPLES --------
num_pad=((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
