def Factorial(number):
    acc = 1
    for i in range(1,number+1):
        acc = acc * i
    return acc
    
result = Factorial(3)
print("La factorielle du nombre entré est ",result)