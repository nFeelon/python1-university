is_logged_in = False
users={"nikita2005": "qwerty", "filon2005": "12345"}

def login():
    username=input("Введите логин: ")
    password=input("Введите пароль: ")
    if username in users.keys() and users[username]==password:
        global is_logged_in
        is_logged_in = True
        return

login()
print(is_logged_in)