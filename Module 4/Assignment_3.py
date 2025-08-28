number = input("Enter a number (or press Enter to quit): ")

smallest = float(number)
largest = float(number)

while number != "":
    if float(number) < smallest:
        smallest = float(number)

    if float(number) > largest:
        largest = float(number)

    number = input("Enter a number (or press Enter to quit): ")

print(f"Smallest number: {smallest:.1f}")
print(f"Largest number: {largest:.1f}")
