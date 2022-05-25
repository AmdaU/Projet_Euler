resultats = {}

for premierNombre in range(1,1000000):
    n,longeurDeChaine = premierNombre,0
    while n != 1:
        if n in resultats:
            longeurDeChaine += resultats[n] -1
            n = 1
        elif n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        longeurDeChaine += 1
    resultats[premierNombre] = longeurDeChaine

list(resultats.values()).index(max(resultats.values())) + 1
