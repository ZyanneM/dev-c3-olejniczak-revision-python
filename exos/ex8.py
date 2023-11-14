import random

def studentDictionary():
    students = {}

    for i in range(1, 11):
        student_name = f"Élève {i}"
        notes = [random.randint(0, 20) for _ in range(3)]
        students[student_name] = notes

    print("Voici les informations sur vos élèves :", students)

    best_student = findBestStudent(students)
    print(f"L'élève avec la meilleure note est : {best_student} avec une note de {max(students[best_student])}")

def findBestStudent(students):
    best_student = max(students, key=lambda student: sum(students[student]))
    return best_student

studentDictionary()