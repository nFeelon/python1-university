file_list = input("Введите имена файлов: ").split()
output_file = input("Введите имя выходного файла: ")
with open(output_file, 'w', encoding='utf-8') as out_file:
    seen = set()
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as in_file:
            for line in in_file:
                line = line.strip()
                if line not in seen:
                    seen.add(line)
                    out_file.write(line + "\n")