import random

def numberList():
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    print("Liste de 10 nombres aléatoires : ", random_numbers)
    largest_number = random_numbers[0]
    for num in random_numbers:
        if num > largest_number:
            largest_number = num
    print("Le plus grand nombre de la liste est : ", largest_number)
    littlest_number = random_numbers[0]
    for num in random_numbers:
        if num < littlest_number:
            littlest_number = num
    print("Le plus petit nombre de la liste est : ", littlest_number)
    average = 0
    sum = 0
    for num in random_numbers:
        sum += num
        average = sum / len(random_numbers)
    print("La moyenne des nombres de la liste est : ", average)


numberList()