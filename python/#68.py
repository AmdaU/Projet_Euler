def permutations(liste):
    if (type(liste == str)):
        liste = list(liste)
    output = []
    if (len(liste) > 1):
        for i in liste:
            copy = liste.copy()
            copy.remove(i)
            miniOut = [i]
            permut = permutations(copy)
            for j in permut:
                miniOutCopy = miniOut.copy()
                if (type(j) != list):
                    j = [j]
                miniOutCopy.extend(j)
                output.append(miniOutCopy)
    else:
        (output.extend(liste))
    return (output)


def sum_str(l):
    out = ""
    for i in l:
        out += str(i)
    return out


sides = [[5+i, 0+i, (1+i) % 5] for i in range(5)]

ps = permutations(range(1, 10+1))

valid = []

for p in ps:
    sums = [sum([p[n] for n in side]) for side in sides]
    if sums[0] == sums[1] == sums[2] == sums[3] == sums[4]:
        valid.append(p)


max_s = 0

for p in valid:
    outer_n = [p[side[0]] for side in sides]
    if outer_n[0] < min(outer_n[1:]):
        string = sum_str([sum_str([p[n] for n in side]) for side in sides])
        if len(string) == 16:
            if int(string) > max_s:
                max_s = int(string)
                sol = p
print(max_s)
