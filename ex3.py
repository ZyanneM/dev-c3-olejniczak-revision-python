def Calculator(str):
    if len(str) == 3:
        if str[0].isdigit() and str[2].isdigit() and str[1] in ['+', '-', 'x', '/']:
            firstOperationNumberA = int(str[0])
            firstOperationNumberB = int(str[2])
        else:
            print("Le premier ou le troisième caractère n'est pas un chiffre ou le deuxième caractère n'est pas un opérateur.")
    else:
        print("Votre opération n'est pas valide")

Calculator("3x3m")
