def fact(x,candidateForFactor = 2):
    facteurs = []
    while candidateForFactor <= x:
        if x % candidateForFactor == 0:
            x /= candidateForFactor
            facteurs += [candidateForFactor]
            candidateForFactor = 1
        candidateForFactor += 1
    return facteurs

mm = lambda l: 1 if not l else l.pop()*mm(l)

def cycle(n,a=0,b=1,c=1):
    liste = []
    while 1:
        f = (c*n**(1/2)+a)//b
        a, b, c = b*b*f-b*a, c*c*n-(a-b*f)**2, b*c

        fa,fb,fc = map(fact,[a,b,c])

        for factor in fa.copy():
            if factor in fb and factor in fc:
                for i in [fa,fb,fc]:
                    i.remove(factor)

        a,b,c = map(mm,[fa,fb,fc])

        if [a,b,c] in liste:
            return len(liste) - liste.index([a,b,c])
        liste.append([a,b,c])

sum([round(i**(1/2))**2 != i and cycle(i)%2 == 1 for i in range(10001)])
