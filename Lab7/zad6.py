import os

with open('data.txt', 'w') as f:
    f.write('')
os.rename('data.txt', 'datadatadata.txt')
os.remove('datadatadata.txt')

try:
    with open('datadatadata.txt', 'r') as f:
        print("Файл не удален")
except FileNotFoundError:
    print("Файл удален")