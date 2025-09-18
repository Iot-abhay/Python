# ====================================
# 🔤 Valid User Name Checker
# ====================================

# ⌨️ Input from user
name = input("Enter your name: ")   

# 📤 Output
if len(name) > 12:
    print("❌ Your username can't be more than 12 letters!")
elif any(char.isdigit() for char in name):
    print("❌ Your username can't contain digits!")
elif " " in name:
    print("❌ Your username can't contain spaces!")
else: 
    print(f"✅ Welcome, {name}!")
