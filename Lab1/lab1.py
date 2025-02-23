import time
import math

# Задание 1

a = input("Введите int: ")
b = input("Введите float: ")
c = input("Введите bool: ")
d = input("Введите str: ")
e = input("Введите smth: ")

print(f"a = {a}, тип = {type(a)}")
print(f"b = {b}, тип = {type(b)}")
print(f"c = {c}, тип = {type(c)}")
print(f"d = {d}, тип = {type(d)}")
print(f"e = {e}, тип = {type(e)}")

f = int(input("Введите int: "))
g = float(input("Введите float: "))
h = bool(input("Введите bool: "))
i = str(input("Введите str: "))
j = input("Введите smth: ")

print(f"f = {f}, тип = {type(f)}")
print(f"g = {g}, тип = {type(g)}")
print(f"h = {h}, тип = {type(h)}")
print(f"i = {i}, тип = {type(i)}")
print(f"j = {j}, тип = {type(j)}")

# Задание 2

a, b, c = 1, 2, 3

# values = [1,2,3]
# a,b,c = values

sum = a+b+c
minus = a-b-c
multiply = a*b*c
divide = a//b
modul = a%b

a, b = b, a

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print("sum = %d" % sum)
print("minus = {}".format(minus))
print(f"multiply = {multiply}")
print(f"divide = {divide}")
print(f"modul = {modul}")

# Задание 3

city = input("Введите название города: ")
temperature = int(input("Введите температуру: "))
print(f"В городе {city} сейчас {temperature}°C")

width = int(input("Введите ширину: "))
height = int(input("Введите высоту: "))
area = width * height
print(f"Площадь прямоугольника с длиной {width} и шириной {height} равна {area}.")

price = float(input("Введите цену: "))
quantity = int(input("Введите количество: "))
sum = price * quantity
print(f"Итоговая стоимость {quantity} товаров по цене {price:.3f} составляет {sum:.3f} рублей.")

sec = int(input("Введите количество секунд: "))
minutes = sec // 60
seconds = sec % 60
print(f"Время {sec} секунд - это {minutes} минут и {seconds} секунд.")

# Задание 4

a = "a"
b = "a"
print(a is b) 

a = "a"
b = "A"
print(a is b)

a = 16
b = 16
print(a is b)

a = 10000
b = 10000
print(a is b) #false, но true - от среды зависит?

# Задание 5

current_time = time.time()
local_time = time.localtime(current_time)

formatted_datetime_1 = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
formatted_date_1 = time.strftime('%d/%m/%Y', local_time)
formatted_time_1 = time.strftime('%H:%M:%S', local_time)

formatted_datetime_2 = time.strftime('%d.%m.%Y %H:%M:%S', local_time)
formatted_date_2 = time.strftime('%d %B %Y', local_time)
formatted_time_2 = time.strftime('%H:%M:%S', local_time)

print(f"Текущая дата и время: {formatted_datetime_1}")
print(f"Дата: {formatted_date_1}")
print(f"Время: {formatted_time_1}")
print()
print(f"Текущая дата и время: {formatted_datetime_2}")
print(f"Дата: {formatted_date_2}")
print(f"Время: {formatted_time_2}")

# Задание 6

angle = float(input("Введите угол в градусах: "))
radians = math.radians(angle)
sin_val = math.sin(radians)
cos_val = math.cos(radians)

print(f"Угол в радианах: {radians:.3f}")
print(f"Синус угла равен {sin_val:.3f}")
print(f"Косинус угла равен {cos_val:.3f}")