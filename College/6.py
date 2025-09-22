# #creating tuple for int, float, string data type
# #Accessing the tuple with hlep of in dex 
# #Tuple slicing with step size
# #Inout function with tuple 
# #tuple operator -> + ,-, *, /
# #how difference b/w list and tuple with example

# #Int
# t1=(1,2,3,4)
# #Float
# t2=(1.1,2.2,3.3,4.4)
# #String
# t3 = ("apple", "banana", "cherry")
# #print
# print(t1)
# print(t2)
# print(t3)

# # acessing 
# print(t1[0])
# print(t2[1])
# print(t3[2])

# #slicing
# print(t1[0:2])
# print(t1[::2])
# print(t1[::-1])

# # Taking tuple input from user

# Convert input string into tuple of integers
t4 = tuple(map(int,input("Enter numbers separated by space: ").split()))
print("Tuple is:", t4)
# String tuple
t5 = tuple(input("Enter numbers separated by space: ").split())
print("Tuple is:", t5)

# #Operators
# a = (1, 2, 3)
# b = (4, 5)
# # Concatenation (+)
# print(a + b)   # (1, 2, 3, 4, 5)
# # Repetition (*)
# print(a * 3)   # (1, 2, 3, 1, 2, 3, 1, 2, 3)

#diff b/w list and tuple

# l=[1,2,3]
# print("Before",l)
# l[1]=100
# print("After",l)

# t=(1,2,3)
# print("Before",t)
# t[1]=100
# print("After",t)



