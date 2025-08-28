import random

random_number = random.randint(1, 10)
guess = int(input("Guess a number (1-10): "))

while True:
    if guess > random_number:
        print("Too high")

    if guess < random_number:
        print("Too low")

    if guess == random_number:
        print("Correct")
        break
    guess = int(input("Guess a number (1-10): "))