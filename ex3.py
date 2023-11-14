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
    if len(str) >= 3:
        numbers = []
        operators = []
        i = 0
        while i < len(str):
            if str[i].isdigit():
                num = ''
                while i < len(str) and str[i].isdigit():
                    num += str[i]
                    i += 1
                numbers.append(int(num))

            if i < len(str) and str[i] in ['+', '-', 'x', '/']:
                operators.append(str[i])
                i += 1
            else:
                break

        if len(numbers) == 3 and len(operators) == 2:
            firstOperation = handleOperation(numbers[0], operators[0], numbers[1])
            secondOperation = handleOperation(firstOperation, operators[1], numbers[2])
            print("Le résultat de l'opération est : ", secondOperation)
        elif len(numbers) == 2 and len(operators) == 1:
            firstOperation = handleOperation(numbers[0], operators[0], numbers[1])
            print("Le résultat de l'opération est : ", firstOperation)
        else:
            print("Votre opération n'est pas valide")
    else:
        print("Votre opération n'est pas valide")

Calculator("100x2+5")
