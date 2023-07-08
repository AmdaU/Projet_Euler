from functools import lru_cache

found_primes = [2]

def addPrime():
    x, index = found_primes[-1]+1, -1
    while found_primes[index := index+1] <= (x)**(1/2):
        if x % found_primes[index] == 0:
            x, index = x+1, -1
    found_primes.append(x)
    return True

@lru_cache(maxsize=2**20)
def partition(a, quantites):
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

N=2
while partition(N := N+1, tuple(found_primes)) <= 5000:
    if (N + 1)  > found_primes[-1]:
        addPrime()

print(N)

