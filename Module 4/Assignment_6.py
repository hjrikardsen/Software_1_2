import random

N = int(input("Random points to generate: "))
n = 0

i = 0
while i < N:
    x = random.random()
    y = random.random()

    if (x ** 2 + y ** 2) < 1:
        n += 1

    i += 1

print(f"Approximation of pi: {(4 * n) / N}")