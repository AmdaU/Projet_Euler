from collections import Counter

liste = [2,2,3]

UwU = Counter(liste)

nombreDeFacteurs = 1

for i in range(len(UwU)):
    nombreDeFacteurs *= UwU[list(UwU)[i]]+1

print(nombreDeFacteurs)
