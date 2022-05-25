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

n = 0
x = 10

def truncate(x):
    truncations = []
    s = str(x)
    for i in range(len(s)-1):
        s = s.replace(s[0],"",1)
        truncations.append(int(s))
    s = str(x)[::-1]
    for i in range(len(s)-1):
        s = s.replace(s[0],"",1)
        truncations.append(int(s[::-1]))
    return truncations

somme = 0

while(n < 11):
    if(estPrem(x)):
        truncatable = True
        for i in truncate(x):
            if(not estPrem(i)):
                truncatable = False
        if(truncatable):
            somme += x
            n += 1
    x += 1

print(somme)
