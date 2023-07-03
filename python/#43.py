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

pan = permutations([0,1,2,3,4,5,6,7,8,9])

div = [2,3,5,7,11,13,17]

somme = 0

for p in range(len(pan)):
    YAS = True
    for i in range(7):
        s = ""
        s += str(pan[p][i+1])
        s += str(pan[p][i+2])
        s += str(pan[p][i+3])
        if(int(s)%div[i] != 0 ):
            YAS = False
    if(YAS):
        s = ""
        for i in pan[p]:
            s += str(i)
        somme += int(s)

print(somme)
