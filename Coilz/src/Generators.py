import random


def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1, 15)


for random_number in lottery():
    print("And the next number is... %d!" % random_number)


def fibonacci(count):
    a, b = 0, 1

    for i in range(count):
        yield b
        a, b = b, a + b


for fib in fibonacci(12):
    print(fib)
