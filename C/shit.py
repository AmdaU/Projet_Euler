def factorize(x):
    if (x <= 1):
        return False
    tested = x
    facteurs = []
    candidateForFactor = 2
    while(candidateForFactor <= tested):
        if(tested % candidateForFactor == 0):
            tested /= candidateForFactor
            facteurs.append(candidateForFactor)
            candidateForFactor = 1
        candidateForFactor += 1
    return facteurs

factorize(906609)
11*83,3*331
