def invers(lst, i=0, j=None, inversions=0):
    if i >= len(lst):
        return inversions
    if j is None:
        j = i + 1
    if j >= len(lst):
        return invers(lst, i + 1, None, inversions)
    if lst[i] > lst[j]:
        inversions += 1
    return invers(lst, i, j + 1, inversions)

lst = [3, 5, 7, 6, 8, 5]
print(invers(lst))
