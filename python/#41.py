def permutations(liste):
    if(type(liste == str)):
        liste = list(liste)
    output = []
    if(len(liste) > 1):
        for i in liste:
            copy = liste.copy()
            copy.remove(i)
            miniOut = [i]
            permut = permutations(copy)
            for j  in permut:
                miniOutCopy = miniOut.copy()
                if (type(j) != list):
                    j = [j]
                miniOutCopy.extend(j)
                output.append(miniOutCopy)
    else:
        (output.extend(liste))
    return(output)

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

n = 9
found = False
biggest = 0

while(not found and n>0):
    for perm in permutations(range(1,n+1)):
        s = ""
        for i in perm:
            s += str(i)
        s = int(s)
        if(estPrem(s) and s > biggest):
            biggest = s
            found = True
    n -= 1

print(biggest)
