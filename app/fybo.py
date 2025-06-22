import random

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for _ in range(3):
    n = random.randint(1, 10)
    print(fibonacci(n))