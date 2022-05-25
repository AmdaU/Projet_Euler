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

n = 3
found = False

while(not found):
    if(not estPrem(n)):
        cant = True
        m = 1
        while(2*m**2 < n and cant):
            cant = not estPrem(n - 2*m**2)
            m+=1
        if(cant):
            found = True
            print(n)
    n+=2
