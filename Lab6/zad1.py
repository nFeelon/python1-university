def capitalize_strings(text: str):
    return text.lower().capitalize()

strl = []
for i in range(5):
    strl.append(input(f"Введите строку {i+1}: "))

print(list(map(capitalize_strings, strl)))