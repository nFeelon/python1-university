# Создайте кортеж temp с дневной температурой каждого дня марта. 
# В кортеже должно быть 31 случайное значений от -10 до 20.
# Сохраните в отдельные кортежи и выведите на экран  значения температур по декадам ( в каждом по 10 значений, в последнем - 11).
# Выведите максимальную и минимальную температуру в каждой неделе неделе с соответствующей надписью. Укажите в какой день она была (0 – понедельник, 1 – вторник и т.д.)

# Найдите среднюю температуру за месяц и выведите её на экран. 

import random
temp = tuple(random.randint(-10, 20) for _ in range(31))
print(temp)

DEC1 = temp[:10]
DEC2 = temp[10:20]
DEC3 = temp[20:]
print(DEC1)
print(DEC2)
print(DEC3)

TmaxW1 = max(temp[:7])
TminW1 = min(temp[:7])

TmaxW2 = max(temp[7:14])
TminW2 = min(temp[7:14])

TmaxW3 = max(temp[14:21])
TminW3 = min(temp[14:21])

TmaxW3 = max(temp[21:28])
TminW3 = min(temp[21:28])

TmaxW4 = max(temp[28:])
TminW4 = min(temp[28:])

print(f"Максимум 1 недели: {TmaxW1} ({temp.index(TmaxW1)})")
print(f"Минимум 1 недели: {TminW1} ({temp.index(TminW1)})")
print(f"Максимум 2 недели: {TmaxW2} ({temp.index(TmaxW2)})")
print(f"Минимум 2 недели: {TminW2} ({temp.index(TminW2)})")
print(f"Максимум 3 недели: {TmaxW3} ({temp.index(TmaxW3)})")
print(f"Минимум 3 недели: {TminW3} ({temp.index(TminW3)})")
print(f"Максимум 4 недели: {TmaxW4} ({temp.index(TmaxW4)})")
print(f"Минимум 4 недели: {TminW4} ({temp.index(TminW4)+28})")

print(f'Средняя температура за месяц = {sum(temp)/len(temp)}')