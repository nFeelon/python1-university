def format_string(template: str, **kwargs):
    for key, value in kwargs.items():
        template = template.replace("{" + key + "}", str(value))
    return template


print(format_string("Привет, {name}!", name="кто-то"))
print(format_string("Мой любимый предмет {subject}.", subject="Python"))
print(format_string("{greeting}, {name}!", greeting="Привет", name="Никита"))
print(format_string("{te{pod}xt}", pod="text", tetextxt="Привет!"))