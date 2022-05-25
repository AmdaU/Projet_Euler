from collections import Counter

def permutations(liste):
    if type(liste == str):
        liste = list(liste)
    output = []
    if len(liste) > 1:
        for i in liste:
            copy = liste.copy()
            copy.remove(i)
            miniOut = str(i)
            permut = permutations(copy)
            for j  in permut:
                miniOutCopy = miniOut
                if type(j) != str:
                    j = str(j)
                miniOutCopy += (j)
                output.append(miniOutCopy)
    else:
        output.extend(liste)

    return(output)

digits = [1,2,3,4,5,6,7,8,9]

def lookForPan(perms):
    prods = []
    somme = 0
    for perm in perms:
        for e1 in range(1,len(perm)-1):
            for e2 in range(e1+1,len(perm)):
                m1 = int(perm[0:e1])
                m2 = int(perm[e1:e2])
                p = int(perm[e2:len(perm)])
                if m1*m2 == p:
                    prods.append(p)
    for i in Counter(prods):
        somme += i
    return somme

lookForPan(permutations([1,2,3,4,5,6,7,8,9]))
