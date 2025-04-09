from functools import reduce
import random

krll = [random.randint(1,10) for _ in range(15)]

above_4 = list(filter(lambda x: x >= 4, krll))
average = reduce(lambda x, y: x + y, krll) / len(krll)
min_mark = reduce(lambda x, y: x if x < y else y, krll)
max_mark = reduce(lambda x, y: x if x > y else y, krll)
above_avg = len(list(filter(lambda x: x > average, krll)))

print(f"Больше или равно 4: {above_4}")
print(f"Среднее: {average:.2f}")
print(f"Минимальная: {min_mark}")
print(f"Максимальная: {max_mark}")
print(f"Выше среднего: {above_avg}")
