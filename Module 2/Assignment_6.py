import random

three_digit_code = f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"

four_digit_code = f"{random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}"

print(f"3-digit code: {three_digit_code}\n4-digit code: {four_digit_code}")