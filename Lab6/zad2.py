import random

numl = [random.randint(-100,100) for _ in range(15)]

def kratno_10(x: int):
    if x%10==0:
        return True
    return False

def kratno_2(x: int):
    if x%2==0:
        return True
    return False

def kratno_3(x: int):
    if x%3==0:
        return True
    return False

print(list(filter(kratno_10, numl)))
print(list(filter(kratno_3, numl)))
print(list(filter(kratno_2, numl)))