# ================================================================================
# ⏳ Countdown Timer
# ================================================================================

import time

# Ask user for total time in seconds
my_time = int(input("Enter time in seconds: "))

# Loop from my_time down to 1
for i in range(my_time, 0, -1):
    sec = i % 60
    minutes = (i // 60) % 60 # // for int divison instead of int() type cast
    hours = i // 3600

    # Format with leading zeros (e.g., 01:05:09)
    print(f"{hours:02}:{minutes:02}:{sec:02}")
    time.sleep(1)  # Wait for 1 second

print("Time's Up!")
