import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

try:
    response = requests.get(url)
    response.raise_for_status()
    posts = response.json()
    print(f"Успешно получено {len(posts)} записей")
    
    print("\nПервые 5 записей:")
    for i, post in enumerate(posts[:5], 1):
        print(f"{i}. Заголовок: {post['title']}")
        print(f"   ID пользователя: {post['userId']}")
        print(f"   ID записи: {post['id']}")
        print(f"   Текст: {post['body'][:100]}...")
        print()
    
    print("\nКомментарии к первому посту:")
    comments_url = f"{url}/1/comments"
    comments_response = requests.get(comments_url)
    comments_response.raise_for_status()
    comments = comments_response.json()
    
    for i, comment in enumerate(comments[:3], 1):
        print(f"{i}. От: {comment['name']} ({comment['email']})")
        print(f"   {comment['body'][:100]}...")
        print()
    
    print("\nСоздание нового поста:")
    new_post = {
        'title': 'Новая версия питона 4.0!!!!',
        'body': 'Скоро студенты будут учить всё заново',
        'userId': 1
    }
    
    post_response = requests.post(url, json=new_post)
    post_response.raise_for_status()
    created_post = post_response.json()
    
    print(f"Пост успешно создан:")
    print(f"ID: {created_post['id']}")
    print(f"Заголовок: {created_post['title']}")
    print(f"Текст: {created_post['body']}")
    
    with open("api_data.json", 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=4)
    print("\nДанные сохранены в файл api_data.json")

except Exception as e:
    print(f"Произошла ошибка: {e}")