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

bimboum = [1,2,3,4,77,4]

swap(bimboum,0,3)

a = False


a,b,c = 1,2,3

(2*9.81*-0.05*(-1 -0.05/-0.1))**0.5



4 - 11/6

'''
1,2
2,3
1,2
1,3
'''

permutations([1,2,3,4])
