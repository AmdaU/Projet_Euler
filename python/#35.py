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

def rot(x):
    rot = []
    s = str(x)
    for i in range(len(s)):
        prem = s[0]
        s = s.replace(prem,"",1)
        s += prem
        rot.append(int(s))
    return rot

somme = 0

for i in range(1000000):
    if(estPrem(i)):
        circular = True
        for r in rot(i):
            if(not estPrem(r)):
                circular = False
        if(circular):
            somme += 1

print(somme)
