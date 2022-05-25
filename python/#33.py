from collections import Counter

def factPrem(x):
    candidateForFactor = 2
    facteursPremiers = []
    nombreDeDiviseurs = 1
    while(candidateForFactor <= x/candidateForFactor):
        if(x % candidateForFactor == 0):
            facteursPremiers.append(candidateForFactor)
            x /= candidateForFactor
            candidateForFactor = 1
        candidateForFactor +=1
    facteursPremiers.append(x)
    return(facteursPremiers)

def simplify(n,d):
    #find prime factors of n and d
    factorsN = Counter(factPrem(n))
    factorsD = Counter(factPrem(d))
    for f in factorsN:
        if(f in factorsD):
            n /= f**min(factorsN[f],factorsD[f])
            d /= f**min(factorsN[f],factorsD[f])
    return(int(n),int(d))

a,b = 1,1

for d in range(11,100):
    for n in range(10,d):
        n = str(n)
        d = str(d)
        if((n[0]) in d):
            #print("bruh")
            n2 = n.replace(n[0],"",1)
            d2 = d.replace(n[0],"",1)
            if(int(d2) != 0 and int(n2)/int(d2) == int(n)/int(d)):
                a *= int(n)
                b *= int(d)
        if((n[1]) in d and int(n[1]) != 0):
            #print("bruh")
            n2 = n.replace(n[1],"",1)
            d2 = d.replace(n[1],"",1)
            if(int(d2) != 0 and int(n2)/int(d2) == int(n)/int(d)):
                a *= int(n)
                b *= int(d)

a,b = simplify(a,b)

print(b)
