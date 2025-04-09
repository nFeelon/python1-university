import random

def generate_password(length=12, use_special_chars=True):
    symbols = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890")
    if use_special_chars:
        symbols.extend(list("!@#$%^&*="))
    new_pass = []
    for _ in range(length):
        new_pass.append(random.choice(symbols))
    return "".join(new_pass)

print(generate_password(use_special_chars=False))
print(generate_password(34))
print(generate_password(10, use_special_chars=False))