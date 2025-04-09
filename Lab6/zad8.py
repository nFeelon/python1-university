def second(strings, index=0, result=None):
    if result is None:
        result = []
    if index >= len(strings):
        return result
    if index % 2 == 0:
        result.append(strings[index][::2])
    return second(strings, index + 1, result)

strings = ['Близнецами', 'называется', 'пара', 'натуральных', 'чисел']
print(second(strings))
