import numpy as np

def concatenatable(a,b):
    return estPrem(int(str(a)+str(b))) and estPrem(int(str(b)+str(a)))

def estPrem(x,candidateForFactor = 2):
    while candidateForFactor*candidateForFactor <= x:
        if x % candidateForFactor == 0: return False
        candidateForFactor += 1
    return True

def nextPrime(x):
    while True:
        x+=1
        if(estPrem(x)):
            return x

currentPrime = 2

primes = {2}
CurentPrimeIsConcatanable = {}

groups = {2:[]}

found = False

while not found:
    for i in primes:
        if concatenatable(currentPrime,i):
            CurentPrimeIsConcatanable[i] = True
            for group in groups[i]:
                canGo = True
                for element in group:
                    if not concatenatable(element,currentPrime):
                        canGo = False
                if canGo:
                    temp = group.copy()
                    temp.add(currentPrime)
                    if len(temp) == 5:
                        found = True
                        print(sum(temp))
                        break
                    groups[i].append(temp)
                    groups[currentPrime].append(temp)
            groups[i].append({currentPrime,i})
            groups[currentPrime].append({currentPrime,i})
        else:
            CurentPrimeIsConcatanable[i] = False
    currentPrime = nextPrime(currentPrime)
    primes.add(currentPrime)
    groups[currentPrime] = []
