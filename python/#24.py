def permutations(liste):
    output = []
    if len(liste) > 1:
        for i in liste:
            copy = liste.copy()
            copy.remove(i)
            for j  in permutations(copy):
                miniOut = [i]
                if type(j) != list:
                    j = [j]
                miniOut.extend(j)
                output.append(miniOut)
    else:
        output.extend(liste)
    return(output)

s = ""
for i in permutations([0,1,2,3,4,5,6,7,8,9])[int(1e6-1)]:
    s += str(i)
int(s)
