from progressbar import ProgressBar

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

def partition(a,quantites):
    partitions = []
    for i in quantites:
        left = a - i
        routes = [i]
        if(left > 0):
            parts = partition(left,quantites)
            for j in parts:
                routesC = routes.copy()
                if (type(j) != list):
                    j = [j]
                routesC.extend(j)
                partitions.append(routesC)
        elif(left == 0):
            partitions.append(routes)
            return partitions
        else:
            return partitions

parts = partition(9,[1,2,3,4,5,6,7,8,9])

parts.remove(parts[-1])

perms = permutations([1,2,3,4,5,6,7,8,9])[::-1]

found = False
x = 0

while not found:
    #prendre un des agencements de chiffres possible
    perm = perms[x]
    #le diviser en segments
    for part in parts:
        n = 0
        segments = []
        for i in part:
            segments.append(perm[n:n+i])
            n += i
        #Convertir les segments d'une liste de nombre a un int
        chiffres = []
        for segment in segments:
            out = ""
            for i in segment:
                out+=str(i)
            chiffres.append(int(out))
        # verifier si tout les parties provienne de la multiplication d'un seul et même facteur
        concatenated = True
        for i in range(1,len(chiffres)):
            if(chiffres[0] != round(chiffres[i]/(i+1))):
                concatenated = False
        if concatenated:
            found = True
            out = ""
            for i in perm:
                out+=str(i)
            print(int(out))
    x += 1
