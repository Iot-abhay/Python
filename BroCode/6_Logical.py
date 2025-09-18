#logical operator = or, and, not


temp=float(input("Enter temperature: "))
# is_rain=bool(input("True for yes and don't write anything for no: "))
is_sunny=bool(input("True for yes and don't write anything for no: "))
# if temp>35 or temp<10 or is_rain:
#     print("Event is Cancelled 😭")
# else:
#     print("Event is Scheduled 😮‍💨")
if temp>35 and is_sunny:
    print("Day is very Hot outside 🥵")
    print("It is sunny 🌞")
elif temp<=0 and is_sunny :  
    print("Day is Cold outside 🥶")
    print("It is sunny 🌞")
elif 0<temp<28 and is_sunny:
    print("Day is very Warm outside 😊")
    print("It is sunny 🌞")
elif 0<temp<28 and not is_sunny:
    print("Day is very Hot outside 🥵")
    print("It is cloudy ☁️")
elif temp<=0 and not is_sunny :  
    print("Day is Cold outside 🥶")
    print("It is cloudy ☁️")
elif 0<temp<28 and not is_sunny:
    print("Day is very Hot outside 😊")
    print("It is cloudy ☁️")
else:
    print("Invalid Input")
    
    