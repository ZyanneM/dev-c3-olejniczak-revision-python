import random

def numberList():
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    print(random_numbers)

numberList()