def estPrem(x,candidateForFactor = 2):
    while candidateForFactor*candidateForFactor <= x:
        if x % candidateForFactor == 0: return False
        candidateForFactor += 1
    return True

gap,number,nbp,nbn = 4,9,3,4
while nbp/nbn > 0.1:
    nbp += sum(1 for i in range(4) if estPrem(number+i*gap))
    number += 4*gap
    nbn +=4
    gap+=2

gap -1
