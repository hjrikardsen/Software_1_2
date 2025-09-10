def get_season(number):
    seasons = {"winter": (12, 1, 2),
               "spring": (3, 4, 5),
               "summer": (6, 7, 8),
               "autumn": (9, 10, 11)}

    for key, value in seasons.items():
        for i in value:
            if i == number:
                return key


month_number = int(input("Enter the number of a month (1-12): "))

if 1 <= month_number <= 12:
    print(f"You entered: {month_number}\nThe season is {get_season(month_number)}.")
else:
    print(f"You entered: {month_number}\nPlease enter a number between 1 and 12.")


