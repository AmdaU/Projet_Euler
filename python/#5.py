num = 1

for x in range(21):
    tested = x
    candidateForFactor = 2
    numCopy = num
    while candidateForFactor <= tested :
        if tested % candidateForFactor == 0:
            if numCopy % candidateForFactor != 0:
                num *= candidateForFactor
                numCopy *= candidateForFactor
            numCopy /= candidateForFactor
            tested /= candidateForFactor
            candidateForFactor = 1
        candidateForFactor += 1

print(num)
