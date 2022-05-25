def estPrem(x):
    if (x <= 1):
        return False
    pasDeFacteur = True
    tested = x
    candidateForFactor = 2
    while(candidateForFactor <= tested/candidateForFactor and pasDeFacteur):
        if(tested % candidateForFactor == 0):
            pasDeFacteur = False
        candidateForFactor += 1
    return pasDeFacteur

def CombienDePremCons(a,b):
    n = 1
    cBo = True
    while cBo:
        x = n**2 + a*n + b
        if estPrem(x):
            n+=1
        else:
            cBo = False
    return(n)

max([[CombienDePremCons(a,b),a*b] for a in range(-1000,1000) for b in range(-1000,1000)])[1]
