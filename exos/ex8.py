import random

def studentDictionary():
    student_names = [("Naruto", "Uzumaki"), ("Sasuke", "Uchiwa"), ("Sakura", "Haruno"), ("Hinata", "Hyuga"), ("Ino", "Yamanaka"), ("Shikamaru", "Nara"), ("Shino", "Aburame"), ("Rock", "Lee"), ("Choji", "Akimichi"), ("Neji", "Hyuga")]

    students = {}

    for i, (first_name, last_name) in enumerate(student_names, start=1):
        notes = [random.randint(0, 20) for _ in range(3)]
        student_key = f"Élève {i}: {first_name} {last_name}"
        students[student_key] = notes

    print("Voici les informations sur vos étudiants :", students)

    best_student = findBestStudent(students)
    print(f"L'étudiant avec la meilleure note est : {best_student} avec une note de {max(students[best_student])}")

def findBestStudent(students):
    best_student = min(students, key=lambda student: (student.split(":")[1].split()[1], student.split(":")[1].split()[0]))
    return best_student

studentDictionary()