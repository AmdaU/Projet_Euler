from collections import Counter

r,count,nombre = 0,2,1

while r < 500:
    nombreCopie = nombre
    candidateForFactor = 2
    facteursPremiers = []
    nombreDeDiviseurs = 1
    while candidateForFactor <= nombreCopie/candidateForFactor:
        if nombreCopie % candidateForFactor == 0:
            facteursPremiers.append(candidateForFactor)
            nombreCopie /= candidateForFactor
            candidateForFactor = 1
        candidateForFactor += 1
    facteursPremiers.append(nombreCopie)

    UwU = Counter(facteursPremiers)
    for i in UwU.values():
        nombreDeDiviseurs *= i+1
    if(nombreDeDiviseurs > r): r = nombreDeDiviseurs

    nombre += count
    count += 1

print(nombre-count+1)
