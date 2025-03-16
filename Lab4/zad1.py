# Создайте программу «Менеджер товаров»
# В списке хранятся товары. Пользователю бесконечно (пока он не ввел «конец») предлагается выбрать действие:
# •	добавить продукт в список
# •	вывести на экран весь список
# •	вывести количество товаров 
# •	удалить по значению
# •	удалить по индексу
# •	заменить один товар на другой (по названию) 
# •	добавить несколько продуктов (вводятся через запятую в одну строку) 
# •	получить комбинацию из N (введенное с клавиатуры (проверяется, что оно меньше общего числа товаров) ) случайных товаров из списка

# Вариант 12

print("Добро пожаловать в менеджер товаров!\n1. Добавить продукт в список\n2. Вывести на экран весь список \n3. Вывести количество товаров \n4. Удалить по значению \n5. Удалить по индексу \n6. Заменить один товар на другой \n7. Добавить несколько продуктов \n8. Получить комбинацию из случайных товаров \n9. Конец")
query = input("Введите запрос: ")

products = []
while query != '9' and query.lower() != 'конец':
    match query:
        case '1':
            product = input("Введите продукт: ")
            products.append(product)
        case '2':
            print(products)
        case '3':
            print(len(products))
        case '4':
            product = input("Введите продукт: ")
            if product in products:
                products.remove(product)
        case '5':
            idx = int(input("Введите индекс: "))
            if idx < len(products):
                del products[idx]
        case '6':
            old_product = input("Введите старый продукт: ")
            new_product = input("Введите новый продукт: ")
            if old_product in products:
                products[products.index(old_product)] = new_product
        case '7':
            products.extend(input("Введите продукты(через запятую): ").split(','))
        case '8':
            n = int(input("Введите количество: "))
            if n < len(products):
                print(random.sample(products, n))
        case _:
            "Неизвестная команда. Повторите попытку"
    query = input("Введите запрос: ")
else:
    print("До свидания!")