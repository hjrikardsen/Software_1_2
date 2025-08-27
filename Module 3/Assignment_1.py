zander = float(input("Enter the length of the zander in centimeters: "))

if zander < 42:
    print("The zander does not meet the size limit.")
    print("Please release the fish back into the lake.")
    print(f"The fish was {round(42 - zander, 2)} centimeters below the size limit.")
else:
    print("The zander meets the size limit.")