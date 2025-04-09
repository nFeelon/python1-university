import json

students = [
    {'name': 'Никита', 'age': 19, 'marks': 85},
    {'name': 'Женя', 'age': 20, 'marks': 92},
    {'name': 'Даник', 'age': 5, 'marks': 88},
    {'name': 'Матвей', 'age': 20, 'marks': 95},
    {'name': 'Вика', 'age': 10000, 'marks': 89},
]

with open('students.json', 'w', encoding='utf-8') as f:
    json.dump(students, f)

with open('students.json', 'r', encoding='utf-8') as f:
    students = json.load(f)

total_count = len(students)
average_age = sum(student['age'] for student in students) / total_count
zadroti = [student for student in students if student['marks'] > 90]

print(f'Общее количество студентов: {total_count}')
print(f'Средний возраст студентов: {average_age:.2f}')
print(f'Студенты с оценками выше 90: {len(zadroti)}')
