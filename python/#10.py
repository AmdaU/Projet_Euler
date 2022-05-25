foundPrimes = [2]

def estPrime(x):
    pasDeFacteur = True
    tested = x
    index = 0
    while foundPrimes[index] <= tested/foundPrimes[index] and pasDeFacteur:
        if tested % foundPrimes[index] == 0:
            pasDeFacteur = False
        index+=1
    if pasDeFacteur:
        foundPrimes.append(x)
    return pasDeFacteur

def nextPrime(x):
    tested = x+1
    while True:
        if estPrime(tested):
            return tested
        tested += 1

p,total = 2,0

while p < 2e6:
    total += p
    p = nextPrime(p)

print(total)
