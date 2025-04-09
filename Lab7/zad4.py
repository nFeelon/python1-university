with open('example2.txt', 'r+', encoding='utf-8') as file:
    text = file.read()
    text = text.replace('Казнить', 'Помиловать').replace('казнить', 'помиловать')
    file.seek(0)
    file.write(text)