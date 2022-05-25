from time import sleep

def partition(a, quantites):
    partitions = []
    for i in quantites:
        left = a - i
        routes = [i]
        if(left > 0):
            parts = partition(left, quantites)
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


par = partition(9, [1,2,9])

par = [p for p in par if len(p) == 3 and len(set(p)) == len(p)][::-1]

ind = [0, 1, 2, 3, 4, len(par)]

found = False

while not found:
    if sum([par[ind[i]][1] == par[ind[(i+1) % 5]][2] for i in range(5)]) == 5:
        found = True

    mov = False
    for i in range(5)[::-1]:
        if ind[i] + 1 < ind[i+1] and not mov:
            ind[i] += 1
            mov = True
        elif ind[i]+5-i == len(par) and ind[i-1]+1 < ind[i] and not mov:
            print('hey')
            i -= 1
            ind[i:5] = range(ind[i]+1, ind[i]+6-i)
            mov = True
    sleep(0.05)
    print(ind)
