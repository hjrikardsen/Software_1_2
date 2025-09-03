import random


def roll_dice():
    return random.randint(1, 6)


isTrue = True
while isTrue:
    result = roll_dice()

    if result == 6:
        print(result)
        isTrue = False
    else:
        print(result)