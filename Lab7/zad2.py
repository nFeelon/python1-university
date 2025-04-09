def analyze_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        unique_words = set(words)
        longest_word = max(words, key=len)
        shortest_word = min(words, key=len)
    
    print(f"Общее количество слов: {len(words)}")
    print(f"Общее количество уникальных слов: {len(unique_words)}")
    print(f"Самое длинное слово: {longest_word}, длина: {len(longest_word)}")
    print(f"Самое короткое слово: {shortest_word}, длина: {len(shortest_word)}")

analyze_file('example.txt')