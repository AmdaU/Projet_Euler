from progressbar import ProgressBar

def estPrem(x):
    if x <= 1:
        return False
    pasDeFacteur = True
    tested = x
    candidateForFactor = 2
    while candidateForFactor <= tested/candidateForFactor and pasDeFacteur:
        if tested % candidateForFactor == 0:
            pasDeFacteur = False
        candidateForFactor += 1
    return pasDeFacteur

primes = []

x = 2

while(x < 1000000/21):
    if(estPrem(x)):
        primes.append(x)
    x += 1

n = 0
l= len(primes)

found = False

pbar = ProgressBar().start()

while(not found):
    pbar.update((len(primes)-l)*100/len(primes))
    for s in range(0,len(primes)-l+1):
        somme = 0
        for p in primes[s:s+l]:
            somme += p
        if(somme < 1000000):
            if(estPrem(somme)):
                found = True
                print(somme)
    l -= 1
pbar.finish()
