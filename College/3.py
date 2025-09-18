# WAP TO PERFORM BITWISE OPERATION ON 5 AND 7

# a=5 #101
# b=7 #111
# 101
# print(f"Result : {a&b}, Result: {a|b}")
# print(f"Result : {a>>b}, Result: {a<<b}")
# print(f"Result : {a>>b}, Result: {a<<b}")
# print("Result :", a&b)

# WAP to Print if both are equal

# a=int(input(f"Enter integer value for a: "))
# b=int(input(f"Enter interger value for b: "))
# if a==b:
#     print("Equal👌🏼")

#WAP to take a radius of circle as input if radius is positive then calculate a curcumference and area of circle

# r=float(input(f"Enter Radius of circle: "))
# pi=3.14
# if r>0:
#     print(f"Area : {pi*r*r}, circumference: {2*pi*r}")

# WAP to Print greater number

# a=int(input(f"Enter integer value for a: "))
# b=int(input(f"Enter interger value for b: "))
# if a>b:
#     print(f"Greater is a: {a}")
# else:
#     print(f"Greater is b: {b}")


# WAP to make salary slip

# sales = float(input("Enter total sales: "))
# basic = 50000

# if sales >= 100000:
#     hra = basic * 0.2
#     da = basic * 1.1
#     conveyance = 1000
#     incentive = sales * 0.1
#     bonus = 10000
# else:
#     hra = basic * 0.1
#     da = basic * 1.1
#     conveyance = 1000
#     incentive = sales * 0.04
#     bonus = 5000

# print("\n------------ Salary Slip -----------")
# print(f"Basic Salary : {basic:.2f}")
# print(f"HRA          : {hra:.2f}")
# print(f"DA           : {da:.2f}")
# print(f"Conveyance   : {conveyance:.2f}")
# print(f"Incentive    : {incentive:.2f}")
# print(f"Bonus        : {bonus:.2f}")


#WAP TO marksheet of student by taking marks of five subject grade should be provided by considering 90 to 100 A

p=int(input("Enter probalilty marks: "))
m=int(input("Enter microcontroller marks: "))
i=int(input("Enter iot marks: "))
e=int(input("Enter edc marks: "))
d=int(input("Enter ds marks: "))

avg=(float) (p+m+i+e+d)/5.0;

if avg>=90:
    print("A+")
elif 80<=avg<=89:
    print("A")
elif 70<=avg<=79:
    print("B")
elif 60<=avg<=69:
    print("C")
elif 50<=avg<=59:
    print("D")
else:
    print("FAIL 🤦🏼 ")