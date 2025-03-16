# Используя методы и операции над множествами, решите три задачи своего варианта.
# •	Напишите программу для определения общего количества различных слов в строке текста.
# •	На вход программе подаются натуральное число nn, а затем nn различных натуральных чисел, каждое на отдельной строке. Напишите программу, которая выводит все общие цифры в порядке возрастания у всех введенных чисел.
# 	Даны по 10-балльной шкале оценки по физике трех учеников. Напишите программу, которая выводит множество оценок третьего ученика, которые не встречаются ни у первого, ни у второго ученика.

# Задача 1
text = input("Введите строку текста: ")
words = text.lower().split()
unique_words = set(words)
print(f"Количество различных слов в тексте: {len(unique_words)}")

# Задача 2
n = int(input("Введите количество чисел: "))
digits_sets = []
for _ in range(n):
    num = input()
    digits = set(map(int, num))
    digits_sets.append(digits)

common = digits_sets[0]
for s in digits_sets[1:]:
    common &= s
    if not common:
        break
    

sorted_common = sorted(common)
print("Общие цифры:", ''.join(map(str, sorted_common)))

# Задача 3
student1 = set(map(int, input("Введите оценки первого ученика через пробел: ").split()))
student2 = set(map(int, input("Введите оценки второго ученика через пробел: ").split()))
student3 = set(map(int, input("Введите оценки третьего ученика через пробел: ").split()))

unique_grades = student3 - (student1 | student2)
print(f"Уникальные оценки третьего ученика: {unique_grades or None}")
