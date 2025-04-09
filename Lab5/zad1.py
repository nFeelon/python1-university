import re

def analyze_text(text: str, case_sensitive=False):
    dtext = dict()
    count_chars = len(text.replace(' ', ''))
    count_props = len(re.findall(r'[.!?]+', text))
    if case_sensitive:
        count_words = len(set(text.split()))
    else:
        count_words = len(set(text.lower().split()))
    dtext = {'Символы': count_chars,
             'Предложения': count_props,
             'Слова': count_words}
    return dtext

print(analyze_text("Hello world, my name is Nikita and I like Python... Также я люблю писать контрольные и отвечать доклады. hello world, my name is nikita and i like python."))

print(analyze_text("Hello world, my name is Nikita and I like Python. Также я люблю писать контрольные и отвечать доклады. hello world, my name is nikita and i like python.", True))