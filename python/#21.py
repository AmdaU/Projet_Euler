from collections import Counter
import numpy as np

def d(a):
    #find primes factors
    tested = a
    candidateForFactor = 2
    factors = []
    while(candidateForFactor <= tested/candidateForFactor):
        if(tested % candidateForFactor == 0):
            factors.append(candidateForFactor)
            tested /= candidateForFactor
            candidateForFactor = 1
        candidateForFactor +=1
    factors.append(tested)

    #find divisors
    count = dict(Counter(factors))
    nDiffFact = len(count)
    diffFact = list(count)
    powers = list(count.values())
    for i in range(len(powers)):
        powers[i] +=1
    divisors = recursiveFor(nDiffFact,powers,mult,[],diffFact[::-1])
    divisors.remove(a)
    #add em up
    result = 0
    for i in divisors:
        result += i
    return result

def mult(outs,data):
    result = 1
    for x in range(len(data)):
        result *= int(data[x]**outs[x])
    return result

def recursiveFor(d,n,function,previousOuts,data):
    outlet = []
    if(d > 0):
        for i in range(n[d-1]):
            l = previousOuts.copy()
            l.append(i)
            outlet.extend(recursiveFor(d-1,n,function,l,data))
    elif(d == 0):
        out = function(previousOuts,data)
        if(type(out) is not list):
            out = [out]
        outlet.extend(out)
        return(outlet)
    return outlet

sum([i for i in range(2,10000) if (d(d(i)) == i and d(i) != i)])
