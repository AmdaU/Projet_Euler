foundPrimes = [2]

def estPrime(x, index=-1):
    while foundPrimes[index := index+1] <= (x)**(1/2):
        if x % foundPrimes[index] == 0:
            return False
    foundPrimes.append(x)
    return True

p, total = 2, 1

while (total := total*p) < 1e6:
    while not estPrime(p := p+1):
        pass

print(total//p)
