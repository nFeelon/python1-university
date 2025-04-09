def generate_report(title, *sections, **options):
    author=options.get("author", "Неизвестен")
    date=options.get("date", "Сегодня")
    report = f"Отчет: {title}\nАвтор: {author}\nДата: {date}\n"
    for section in sections:
        report += section + "\n"
    return report

print(generate_report("Лабы", "Общая количество лаб: 1000", "Самые лучшие лабы: Python", author="Филон Никита", date="Вчера"))
print(generate_report("Работа", "Общее количество циклов: 9999", "Самый популярный товар: Функции", date="Завтра"))