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

tri = lambda n: n*(n+1)//2
squ = lambda n: n*n
pent = lambda n: n*(3*n-1)//2
hex = lambda n: n*(2*n-1)
hept = lambda n: n*(5*n-3)//2
oct = lambda n: n*(3*n-2)

polyg = [tri,squ,pent,hex,hept,oct]

dic = dict({})

found = False

for pol in polyg:
    n = 1
    dic[pol] = {}
    while len(str(pol(n)))<4:
        n+=1
    while len(str(pol(n)))<5:
        if str(pol(n))[0:2] not in dic[pol].keys():
            dic[pol][str(pol(n))[0:2]] = []
        dic[pol][str(pol(n))[0:2]].append(str(pol(n))[2:4])
        n+=1

polyg.remove(tri)
perms = permutations(polyg)

for t in dic[tri].items():
    key = t[0]
    for a in t[1]:
        for pol in perms:
            if a in dic[pol[0]].keys():
                for b in dic[pol[0]][a]:
                    if b in dic[pol[1]].keys():
                        for c in dic[pol[1]][b]:
                            if c in dic[pol[2]].keys():
                                for d in dic[pol[2]][c]:
                                    if d in dic[pol[3]].keys():
                                        for e in dic[pol[3]][d]:
                                            if e in dic[pol[4]].keys():
                                                for f in dic[pol[4]][e]:
                                                    if f == key:
                                                        print((int(a)+int(b)+int(c)+int(d)+int(e)+int(f))*101)
