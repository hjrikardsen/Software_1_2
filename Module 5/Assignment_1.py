import random

dices = int(input("How many dice to roll: "))

sum_dices = 0

for i in range(0, dices):
    dice = random.randint(1, 6)
    sum_dices += dice

print(f"Sum of the dice: {sum_dices}")