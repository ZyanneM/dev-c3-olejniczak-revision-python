def StringData():
    string = input("Saisissez une phrase : ")
    lastchar = string[-1]
    if len(string) < 10:
        print("La phrase est trop courte")
    elif lastchar not in ['.', '?', '!']:
        print("La phrase ne se termine pas par un signe de ponctuation")
    elif not isinstance(string, str):
        print("La phrase n'est pas une chaine de caractères")

StringData()