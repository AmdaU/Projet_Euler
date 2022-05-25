from collections import Counter

def mult(outs,data):
    result = 1
    for x in range(len(data)):
        result *= int(data[x]**outs[x])
    return result

def recursiveFor(d,n,function,previousOuts,data):
    outlet = []
    if d > 0:
        for i in range(n[d-1]):
            l = previousOuts.copy()
            l.append(i)
            outlet.extend(recursiveFor(d-1,n,function,l,data))
    elif d == 0:
        out = function(previousOuts,data)
        if type(out) is not list:
            out = [out]
        outlet.extend(out)
        return(outlet)
    return outlet

def primeFactrize(a):
    tested = a
    index = 0
    candidateForFactor = 2
    factors = []
    while(candidateForFactor <= tested/candidateForFactor):
        if(tested % candidateForFactor == 0):
            factors.append(candidateForFactor)
            tested /= candidateForFactor
            candidateForFactor = 1
        candidateForFactor += 1
    factors.append(round(tested))
    return factors

def factorize(x):
    count = Counter(primeFactrize(x))
    nDiffFact = len(count)
    diffFact = list(count)
    powers = [list(count.values())[i]+1 for i in range(nDiffFact)]
    return recursiveFor(nDiffFact,powers,mult,[],diffFact[::-1])

xi = 28123

abondants = [a for a in range(1,xi) if(sum([i for i in factorize(a)])-a>a)]

nombreDab = set(abondants[i] + abondants[j] for i in range(len(abondants)) for j in range(i+1) if abondants[i] + abondants[j] <= xi)

int(xi*(xi + 1)/2 - sum(list(nombreDab)))
