from time import time
start_time = time()

foundPrimes = [2]

def estPrime(x, index=-1):
    while foundPrimes[index := index+1]**2 <= (x):
        if x % foundPrimes[index] == 0:
            return False
    foundPrimes.append(x)
    return True

p, total = 2, 1

while p < 1e5:
    while not estPrime(p := p+1):
        pass

print(time()-start_time)
print(foundPrimes)
