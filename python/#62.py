isCube = lambda n: n == round(n**(1/3))**3

n = 0
found = False
shits = {}

while not found:
    n+=1
    reps = set({})
    s = str(n**3)
    for i in set(str(n**3)):
        b = 0
        while i in s:
            b +=1
            s = s.replace(i,"",1)
        reps.add((i,b))
    reps = frozenset(reps)
    if reps not in shits.keys():
        shits[reps] = [n]
    else:
        shits[reps].append(n)
        if len(shits[reps]) == 5:
            found = True
            print(int(shits[reps][0])**3)
