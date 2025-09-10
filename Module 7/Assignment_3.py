
airports = {}

isTrue = True

while isTrue:
    print("\nAirport Data Management")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")
    option = input("Please choose an option (1-3): ")

    if option == "1":
        key = input("Enter the ICAO code: ")
        value = input("Enter the airport name: ")

        airports[key] = value
        print(f"Airport {value} with ICAO code {key} has been added.")
    elif option == "2":
        key = input("Enter the ICAO code: ")

        if key in airports.keys():
            print(f"The airport with ICAO code {key} is {airports[key]}.")
        else:
            print(f"No airport found with ICAO code {key}.")
    elif option == "3":
        print("Thank you for using the Airport Data Management system. Goodbye!")
        isTrue = False