from collections import Counter

def factorize(x):
    if (x <= 1):
        return False
    tested = x
    facteurs = []
    candidateForFactor = 2
    while(candidateForFactor <= tested):
        if(tested % candidateForFactor == 0):
            tested /= candidateForFactor
            facteurs.append(candidateForFactor)
            candidateForFactor = 1
        candidateForFactor += 1
    return facteurs

found = False
n = 2

nums = [0,0,0,0]

while(not found):
    nums[0] = nums[1]
    nums[1] = nums[2]
    nums[2] = nums[3]
    nums[3] = (len(Counter(factorize(n))))
    if(Counter(nums)[4] == 4):
        found = True
        print(n-3)
    n+=1

for i in range(4):
    print(factorize(134043+i))
