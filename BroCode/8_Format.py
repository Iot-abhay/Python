# ================================================================================
# 🔤 Format Specifier in Python: {value:flags}
# Flags control how the value is displayed (width, alignment, precision, signs, commas)
# ================================================================================

a1 = 2345.3
a2 = -3.456
a3 = 4523.45345

print(f"A1 is {a1:10}")        # Width 10 (right-aligned by default)
print(f"A1 is {a1:010}")       # Width 10, padded with 0
print(f"A2 is {a2:.1f}")       # 1 decimal place
print(f"A1 is {a1:>10}")       # Right-align in width 10
print(f"A2 is {a2:<10}")       # Left-align in width 10
print(f"A3 is {a3:^10}")       # Center-align in width 10
print(f"A1 is {a1:+}")         # Always show sign (+ or -)
print(f"A2 is {a2:+}")         # Always show sign (+ or -)
print(f"A3 is {a3:+}")         # Always show sign (+ or -)
print(f"A1 is {a1:,}")         # Add comma as thousand separator
print(f"A1 is {a1:+,.2f}")     # Sign + comma + 2 decimal places
print(f"A2 is {a2:+,.2f}")     # Sign + comma + 2 decimal places
print(f"A3 is {a3:+,.2f}")     # Sign + comma + 2 decimal places
