with open('example.txt', 'w', encoding='utf-8') as f:
    f.write('Привет, мир!\n')
    f.write('Сегодня я делаю лабу по питону\n')
    f.write('Хорошо, что я учу питон.\n')
    f.write('Ура!')

# 1 способ
with open('example.txt', 'r', encoding='utf-8') as f:
    data = f.read()
print(data)

# 2 способ
with open('example.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
print(data)

# 3 способ
with open('example.txt', 'r', encoding='utf-8') as f:
    data = f.readline()
    while data:
        print(data, end='')
        data = f.readline()

# 4 способ
with open('example.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')
