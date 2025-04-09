def classify_numbers(*args, threshold=0):
    positive = []
    negative = []
    zero = []
    for num in args:
        if num > threshold:
            positive.append(num)
        elif num < threshold:
            negative.append(num)
        else:
            zero.append(num)
    return [positive, negative, zero]

print(classify_numbers(1, -1, 0, 5, -5, 0, threshold=0))
print(classify_numbers(1, -1, 0, 5, -5, 0, threshold=2))