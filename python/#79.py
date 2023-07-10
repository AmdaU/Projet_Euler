conds = set()
nums = set()

with open('keylog.txt') as file:
    for line in file:
        nums.update(*line.strip())
        conds.add((line[0], line[1]))
        conds.add((line[1], line[2]))


for cond in conds:
    if cond[::-1] in conds:
        print('code will not work')

def permutations(liste):
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

def check_perm(perm):
    for cond in conds:
        ind = perm.index(cond[0])
        if not cond[1] in perm[ind:]:
            return False
    return True

print(conds)

for perm in permutations(nums):
    if check_perm(perm):
        break

print(''.join(perm))

