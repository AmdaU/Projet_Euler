def estPrime(x, factor_candidate = 2):
    return factorize(x, [], 2)[0] == x

def factorize(x, factors, factor_canditate):
    while(factor_canditate*factor_canditate <= x):
        if (res := divmod(x,factor_canditate))[1] == 0:
            x = res[0]
            factors.append(factor_canditate)
        else:
            factor_canditate += 1
    return factors + [x]

def ETF(factors):
    out = 1
    for factor in set(factors):
        out *= factor**(factors.count(factor)-1)*(factor-1)
    return out

def isPerm(a,factors):
    a, b = list(str(a)), list(str(ETF(factors)))
    a.sort()
    b.sort()
    return a == b

# Computes a lower bound
def search_best_factors(np, n):
    if np == 1:
        while not estPrime(n:=n-1):
            pass
        yield [n]
    else:
        p1 = int(n**(1/np))+1
        while p1 > 1:
            while not estPrime(p1:=p1-1):
                pass
            for pns in search_best_factors(np-1, (n//p1)+1):
                yield [p1] + pns

for factors in search_best_factors(2, int(1e7)):
    i = factors[0]*factors[1]
    if isPerm(i, factors):
        break

low_score, lowest_scorer = i/ETF(factors), i
p = int(low_score/(low_score-1))

#search through all prime sufficiently large to achive lower bound
while p < 1e7**(0.5):
    p2 = int(1e6//p)-1
    while (i:=p2*p) < 1e7:
        factors = [p,p2]
        if isPerm(i, factors):
            score = i/ETF(factors)
            if score < low_score:
                low_score, lowest_scorer = score, i
        while not estPrime(p2:=p2+1):
            pass
    while not estPrime(p:=p+1):
        pass

print(lowest_scorer)
