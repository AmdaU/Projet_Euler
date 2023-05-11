foundPrimes = [2]


def estPrime(x, index=-1):
    while foundPrimes[index := index+1] <= (x)**(1/2):
        if x % foundPrimes[index] == 0:
            return False
    foundPrimes.append(x)
    return True


def nextPrime(x):
    while not True:
        if estPrime(x := x+1):
            return x


p, total = 2, 1

while (total := total*p) < 1e6:
    p = nextPrime(p)

print(total//p)
