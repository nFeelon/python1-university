# Подключите модуль collections. Решите представленные задачи используя namedtuple,defaultdic,Counter.
# Создайте программу, в которой вы будете использовать namedtuple из модуля collections для управления информацией о студентах. Определите именованный кортеж Student, который будет содержать поля: 
# name (имя студента),
# age (возраст студента), 
# grade (оценка студента) 
# email (электронная почта студента).
# Создайте список студентов, добавив несколько экземпляров Student. 
# Выведите информацию о всех студентах в удобочитаемом формате.
# Найдите и выведите информацию о конкретном студенте по его имени.
# Отредактируйте информацию об одном студенте.
# Реализуйте сортировку списка студентов по имени или возрасту и выведите отсортированный список.

import collections
from typing import Counter

# Задание 1

Student = collections.namedtuple('Student', ['name', 'age', 'grade', 'email'])

Student1 = Student("Nikita", 19, 8, 'n@f.by')
Student3 = Student("Zikita", 20, 9, 'm@f.by')
Student2 = Student("Yikita", 21, 10, 'y@f.by')

spisok = [Student1, Student2, Student3]

for stud in spisok:
    print(f'Имя: {stud.name}, Возраст: {stud.age}, Оценка: {stud.grade}, Почта: {stud.email}')

finder = input("Введите имя студента: ")
for stud in spisok:
    if stud.name == finder:
        print(f"Найден студент: {stud.name}, Возраст: {stud.age}, Оценка: {stud.grade}, Почта: {stud.email}")
        break
else:
    print(f"Студент с именем {finder} не найден")

new_student = spisok[0]._replace(name='Andrew')
spisok[0] = new_student
print(spisok[0])

sorted_by_name = sorted(spisok, key=lambda x: x.name)
print("\nСписок, отсортированный по имени:")
for stud in sorted_by_name:
    print(f'Имя: {stud.name}, Возраст: {stud.age}, Оценка: {stud.grade}, Почта: {stud.email}')

sorted_by_age = sorted(spisok, key=lambda x: x.age)
print("\nСписок, отсортированный по возрасту:")
for stud in sorted_by_age:
    print(f'Имя: {stud.name}, Возраст: {stud.age}, Оценка: {stud.grade}, Почта: {stud.email}')

# Задание 2

note = collections.defaultdict(int)
note['Nikita'] +=1
note['Eugene'] +=1
note['Daniel'] +=1
note['Mateusz'] +=1

for i in note:
    print(f'Имя: {i}, Пропуски: {note[i]}')

finder2 = input("Введите имя: ")
print(f'Имя: {finder2}, Пропуски: {note[finder2]}')

# Задание 3

text = "Привет мой дорогой друг. Привет мой друг. Привет. А А Ау Привет б б ф ы а н ф ы ы ы".replace('.', ' ').split()
ctx = Counter(text)
print(ctx)

print("Пять самых частых слов:")
for word, count in ctx.most_common(5):
    print(f"Слово '{word}' встречается {count} раз")

search_word = input("Введите слово для поиска: ")
print(f"Слово '{search_word}' встречается {ctx[search_word]} раз")