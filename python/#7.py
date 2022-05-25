foundPrimes,x = [2],3

while len(foundPrimes) <= 1e4:
    pasDeFacteur = True
    tested = x
    index = 0
    while(foundPrimes[index] <= tested/foundPrimes[index] and pasDeFacteur):
        if(tested % foundPrimes[index] == 0):
            pasDeFacteur = False
        index += 1
    if(pasDeFacteur):
        foundPrimes.append(x)
    x += 1
print(foundPrimes[-1])
