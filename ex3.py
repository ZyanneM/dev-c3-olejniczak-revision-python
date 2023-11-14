def handleOperation(number1, operator, number2):
    if operator == 'x':
        return number1 * number2
    elif operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '/':
        return number1 / number2

def Calculator(str):
    if len(str) == 3:
        if str[0].isdigit() and str[2].isdigit() and str[1] in ['+', '-', 'x', '/']:
            firstOperationNumberA = int(str[0])
            firstOperationNumberB = int(str[2])
            firstOperation = handleOperation(firstOperationNumberA, str[1], firstOperationNumberB)
            print("Le résultat de l'opération est : ", firstOperation)
        else:
            print("Le premier ou le troisième caractère n'est pas un chiffre ou le deuxième caractère n'est pas un opérateur.")
    elif len(str) == 5:
        if str[0].isdigit() and str[2].isdigit() and str[4].isdigit() and str[1] in ['+', '-', 'x', '/'] and str[3] in ['+', '-', 'x', '/']:
            firstOperationNumberA = int(str[0])
            firstOperationNumberB = int(str[2])
            secondOperationNumber = int(str[4])
            firstOperation = handleOperation(firstOperationNumberA, str[1], firstOperationNumberB)
            secondOperation = handleOperation(firstOperation, str[3], secondOperationNumber)
            print("Le résultat de l'opération est : ", secondOperation)
        else:
            print("Le premier, le troisième ou le cinquième caractère n'est pas un chiffre ou les opérateurs sont incorrects.")
    else:
        print("Votre opération n'est pas valide")

Calculator("34+2")
