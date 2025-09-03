number = int(input("Enter an integer: "))

isPrime = True

if number == 0 or number == 1:
    print(f"{number} is not a prime number.")

elif number == 2:
    print(f"{number} is a prime number.")

else:
    for i in range(1, number):

        if number % i == 0 and i != 1 and i != number:
            isPrime = False
            break

    if isPrime == False:
        print(f"{number} is not a prime number.")
    else:
        print(f"{number} is a prime number.")