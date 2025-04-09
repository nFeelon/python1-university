def sumNumbers(s: str):
    result = 0
    currentNumber = ''
    for char in s:
        if char.isdigit():
            currentNumber += char
        elif currentNumber != '':
            result += int(currentNumber)
            currentNumber = ''
    if currentNumber != '':
        result += int(currentNumber)
    return result


print(sumNumbers("0012 . 3e-1000"))
print(sumNumbers("aa11b33"))
print(sumNumbers("hello world 123"))
