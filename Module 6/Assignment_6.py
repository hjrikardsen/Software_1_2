import math


def calculate_unit_price(diameter, price):
    diameter_m = diameter / 100
    area = math.pi * (diameter_m / 2) ** 2
    return price / area


diameter1 = float(input("Enter the diameter of the first pizza (cm): "))
price1 = float(input("Enter the price of the first pizza (euros): "))

diameter2 = float(input("Enter the diameter of the second pizza (cm): "))
price2 = float(input("Enter the price of the second pizza (euros): "))

print(f"Unit price of the first pizza: {calculate_unit_price(diameter1, price1):.2f} euros/m²")
print(f"Unit price of the second pizza: {calculate_unit_price(diameter2, price2):.2f} euros/m²")

if calculate_unit_price(diameter1, price1) < calculate_unit_price(diameter2, price2):
    print("The first pizza provides better value for money.")
else:
    print("The second pizza provides better value for money.")