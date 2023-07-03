found_primes = [2]

def ETF(x):
    factors, index, factor_candidate, out = [], 0, found_primes[0], 1
    while(factor_candidate*factor_candidate <= x):
        if (res := divmod(x,factor_candidate))[1] == 0:
            x = res[0]
            factors.append(factor_candidate)
        else:
            factor_candidate = found_primes[index:=index+1]
    if factors == []:
        found_primes.append(x)
    factors += [x]
    for factor in set(factors):
        out *= factor**(factors.count(factor)-1)*(factor-1)
    return out

print(sum([ETF(i) for i in range(2, int(1e6))]))

