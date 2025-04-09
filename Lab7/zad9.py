import json

def load_data(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)

def add_product(data, name, price, count):
    for product in data:
        if product['name'] == name:
            product['count'] += count
            return
    data.append({'name': name, 'price': price, 'count': count})

filename = 'products.json'
data = load_data(filename)
add_product(data, 'Хлэб', 10, 10)
add_product(data, 'Вода', 1, 5)
save_data(data, filename)