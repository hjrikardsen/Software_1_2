import random


def roll_dice(sides):
    return random.randint(1, sides)


user_sides = int(input("Enter sides of dice: "))

isTrue = True
while isTrue:
    result = roll_dice(user_sides)

    if result == user_sides:
        print(result)
        isTrue = False
    else:
        print(result)