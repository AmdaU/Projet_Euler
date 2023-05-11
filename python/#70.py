def fact(x, candidateForFactor=2) -> list[int]:
    facteurs = [1]
    while candidateForFactor <= (x)**(1/2)+1:
        if x % candidateForFactor == 0:
            x //= candidateForFactor
            facteurs += [candidateForFactor]
            candidateForFactor -= 1
        candidateForFactor += 1
    if x > 1:
        facteurs += [x]
    return facteurs


print(fact(87109))
