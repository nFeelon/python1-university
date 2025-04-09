def median(*args):
    data = list(args)
    data.sort()
    n = len(data)
    if n % 2 == 1:
        return data[n // 2]
    else:
        return (data[n // 2 - 1] + data[n // 2]) / 2
    

print(median(1, 3, 5))
print(median(2, 4, 6, 8))
print(median(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
