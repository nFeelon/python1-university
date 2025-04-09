from functools import reduce
import random

numl = [random.randint(1,10) for _ in range(5)]

print(numl)
print(reduce(lambda x,y: x*y, numl))