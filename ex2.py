def StringData():
    string = input("Saisissez une phrase : ")
    lastChar = string[-1]
    if string.isdigit():
        print("Votre phrase ne contient que des nombres.")
    elif lastChar not in ['.', '?', '!']:
        print("Votre phrase est incorrecte : elle doit se terminer par un signe de ponctuation.")
    else:
        print("Votre phrase est valide, voici votre phrase en majuscule : ", string.upper())

StringData()