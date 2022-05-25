from functools import reduce

N = [
lambda n : n*(n+1)/2,
lambda n : n**2,
lambda n : n*(3*n - 1)/2,
lambda n : n*(2*n - 1),
lambda n : n*(5*n - 3)/2,
lambda n : n*(3*n - 2)
]

def lim(func):
    n = 0
    while func(n)<10**4+1: n += 1
    return n

Pool = [[i(n) for n in range(lim(i)) if len(str(int(i(n)))) == 4] for i in N]
Test = [[[str(i)[0:2], str(i)[2:4]] for i in k] for k in Pool]
L = len(Test)

def Glue(x, y):
    GluedLists = []
    for i in x:
        for j in y:
            if i[-1] == j[0]:
                GluedLists.append(i + j)
    return GluedLists


def perm(choices, elem = [[]]):
    if (len(elem[0]) == len(choices)):
        return elem
    newelem = []
    for i in elem:
        for j in choices - set(i):
            newelem.append(i+[j])
    return perm(choices, elem = newelem)

Indices = perm(set(range(L)))
PermTest = [[Test[i] for i in j] for j in Indices]

for i in PermTest:
    Paths = reduce(Glue, i)
    for j in Paths:
        if j[-1] == j[0]:
            Result = 0
            for k in range(L):
                Result += int(j[2*k] + j[2*k+1])
            break

print(Result)
