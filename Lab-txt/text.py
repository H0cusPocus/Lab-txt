import json

# Створення файлу 1.txt з мовами програмування
languages = ["JavaScript", "Python", "Java", "C++", "Ruby"]
with open("1.txt", "w") as file:
    json.dump(languages, file)

# Створення файлу 2.txt з прізвищами студентів
students = ["Smith", "Johnson", "Brown", "Davis", "Miller"]
with open("2.txt", "w") as file:
    json.dump(students, file)