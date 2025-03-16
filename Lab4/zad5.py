# Решите представленные задачи с помощью словарей.

# 1. Напишите программу, которая будет превращать натуральное число в строку, заменяя все цифры в числе на слова:


num_dict = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

num = int(input())
res = ''
for digit in str(num):
    res += num_dict[int(digit)] + ' '
print(res[:-1])

# 2.  Код Морзе для представления цифр и букв использует тире и точки.
# Напишите программу для кодирования текстового сообщения “ваше ФИО” в соответствии с кодом Морзе.

morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', 
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': ' '
}

name = input()
morse_result = ''

for char in name:
    if char.upper() in morse_code:
        morse_result += morse_code[char.upper()] + ' '
    elif char == ' ':
        morse_result += '/ '

print(f"Текст: {name}")
print(f"Код Морзе: {morse_result}")

# 3. На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего, без учета регистра. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

stroka = input()
words = stroka.lower().split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

min_count = min(word_count.values())
rare_words = [word for word, count in word_count.items() if count == min_count]
rare_words.sort()

print(f"Самое редкое слово: {rare_words[0]}")
