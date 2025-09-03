def gallons_to_liters(gallons):
    return gallons * 3.785


isTrue = True

while isTrue:
    gallons = float(input("Enter a volume in American gallons (negative value to quit): "))

    if gallons < 0:
        isTrue = False
    else:
        print(f"{gallons:.1f} American gallons is {gallons_to_liters(gallons):.2f} liters.")

print("Program finished.")