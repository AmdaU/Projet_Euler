from functools import lru_cache

@lru_cache(maxsize=2**20)
def partition(a,quantites):
    numberOfWays = 0
    for i in quantites:
        left = a - i
        if left > 0:
            numberOfWays += partition(left,quantites[quantites.index(i):])
        elif left == 0:
            return numberOfWays+1
        else:
            return numberOfWays
    return numberOfWays

print(partition(100, range(1, 100) ))
