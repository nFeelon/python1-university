import requests
from bs4 import BeautifulSoup
import json

url = "https://ria.ru/lenta/"

try:
    response = requests.get(url)
    response.raise_for_status()
    html = response.text
except Exception as e:
    print(f"Ошибка при загрузке страницы: {e}")
    exit(1)

soup = BeautifulSoup(html, 'html.parser')
news_list = []
news_items = soup.find_all('a', class_='list-item__title')

for item in news_items:
    title = item.text.strip()
    link = item.get('href')
    if link:
        link = f"https://ria.ru{link}"
    
    news_list.append({
        'title': title,
        'link': link,
    })

if not news_list:
    print("Новости не найдены")
    exit(1)

print(f"Найдено {len(news_list)} новостей:\n")
for i, news in enumerate(news_list, 1):
    print(f"{i}. {news['title']}")
    print(f"   Ссылка: {news['link']}")
    print()

try:
    with open("news.json", 'w', encoding='utf-8') as f:
        json.dump(news_list, f, ensure_ascii=False, indent=4)
    print(f"Новости сохранены в файл news.json")
except Exception as e:
    print(f"Ошибка при сохранении в файл: {e}")