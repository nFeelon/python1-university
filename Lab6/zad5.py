def palindrom(x: str):
    if x[0] != x[len(x)-1]:
        return False
    elif len(x)<=3:
        return True
    else:
        return palindrom(x[1:len(x)-1])

print(palindrom("hhahh"))
print(palindrom("ahsha"))
print(palindrom("ahsha1"))

# Можно в одну строчку без рекурсии x == x[::-1] =) 