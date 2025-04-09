import os

N = int(input("Введите количество папок: "))

for i in range(1, N + 1):
    os.mkdir(f"PRIM/prim{i}")

os.rmdir(f"PRIM/prim{2}")
os.rmdir(f"PRIM/prim{4}")
