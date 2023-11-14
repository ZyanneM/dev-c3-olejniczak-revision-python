import random

def studentDictionary():
    students = {}

    for i in range(1, 11):
        student_name = f"Élève {i}"
        notes = [random.randint(0, 20) for _ in range(3)]
        students[student_name] = notes

    print("Voici les informations sur vos élèves :",students)

studentDictionary()