tested = 600851475143

candidateForFactor = 1
while(candidateForFactor <= tested/candidateForFactor):
    if(tested % candidateForFactor == 0):
        tested /= candidateForFactor
        candidateForFactor = 1
    candidateForFactor += 1

print(int(tested))
