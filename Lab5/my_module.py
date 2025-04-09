import random

def randomList(n: int):
    return [random.randint(-99,99) for _ in range(n)]

def randomMatrix(n: int):
    return [[random.randint(0,9) for _ in range(n)] for _ in range(n)]

def maxLength(x: list):
    maxl = 0
    maxw = ''
    for i in x:
        if len(i)>maxl:
            maxl=len(i)
            maxw = i
    return maxw

def currentSums(x: list):
    result = []
    s = 0
    for i in x:
        s += i
        result.append(s)
    return result

def threeSimbol(s: str):
    result = []
    for i in range(len(s)-2):
        result.append(s[i:i+3])
    return result