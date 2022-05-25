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

found = False

n1 = 1
num = ""
while(not found and n1 < 10):
    n2 = n1
    while(not found and n2 < 10):
        n3 = n2
        while(not found and n3 < 10):
            n4 = n3
            while(not found and n4 < 10):
                permsl = permutations([n1,n2,n3,n4])
                perms = []
                permss = []
                for p in permsl:
                    s = ""
                    for i in p:
                        s += str(i)
                    perms.append(int(s))
                    permss.append(s)
                for i in range(22):
                    for j in range(i+1,23):
                        for k in range(j+1,24):
                            if(estPrem(perms[i]) and estPrem(perms[j]) and estPrem(perms[k])):
                                if(perms[i]-perms[j] == perms[j] - perms[k] and perms[i] != 1487 and perms[j] - perms[k] != 0):
                                    found = True
                                    num = permss[i]+permss[j]+permss[k]
                n4+=1
            n3+=1
        n2+=1
    n1+=1

print(num)
