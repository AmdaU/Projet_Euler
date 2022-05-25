import numpy as np

def estPrem(x,candidateForFactor = 2):
    while candidateForFactor*candidateForFactor <= x:
        if x % candidateForFactor == 0: return False
        candidateForFactor += 1
    return True

concatenatable = lambda a,b: estPrem(int(str(a)+str(b))) and estPrem(int(str(b)+str(a)))

def nextPrime(x):
    while True:
        x+=1
        if(estPrem(x)):
            return x

currentPrime = 2

primes = {2}

groups = [{2}]

CurentPrimeIsConcatanable = {}

found = False

while not found:
    for p in primes:
        CurentPrimeIsConcatanable[p] = concatenatable(p,currentPrime)
    for group in groups.copy():
        if np.all([CurentPrimeIsConcatanable[q] for q in group]):
            temp = group.copy()
            temp.add(currentPrime)
            if len(temp) == 5:
                found = True
                print(sum(temp))
            groups.append(temp)

    currentPrime = nextPrime(currentPrime)
    primes.add(currentPrime)
    groups.append({currentPrime})



'''
---------- Fun Facts ------------
-2 et 5 ne peuvent jamais faire partie d'un tel groupe si on utilise la base 10

    Preuve:
    Soit le groupe {a,2} où a est un entier naturel quelquonque différent de 2:

        a concatenate 2 = a2      (Attention ici de ne pas confondre concatenate
                                    avec un multiplication implicite, par
                                    exemple si a = 10, a2 = 102 \neq 20  !)
                        = 10*a + 2
                        = 2*5*a + 2
                        = 2*(5*a + 1)
                        = 2*b

        (où b = 5*a+1)

    On a donc que (a concatenate 2) s'écrit comme le mutiple de deux nombre
    entiers est n'est donc pas premier et ce peu importe la valeur de a. Il en
    va exactement de même avec le nombre premier 5.



-Le mod 3 de la somme des dicimale des nombres d'un même groupe doit toujours
être le même (ou 0, dans le cas ou 3 fait partie du groupe)

        En effet, si la somme des décimale d'un nombre est divisible par 3, le
    nombre complet l'est lui aussi (Du moins c'est vrai en base 10). Aussi la
    somme des décimales d'un nombre provenant de l'opération concatenate, sera
    évidemment la somme des décimales des deux nombres qui ont servis à générer
    ce nombre.

        On apelle maintenant la somme des décimales d'une nombre x S_x et on a
    les deux nombres premiers a et b. On définis aussi c comme étant
    c = a concatenate b. On peut écrire la propriété discuté plus haut comme
    (Si S_x%3 = 0, alors x%3 = 0)

    Découlant de la propriété discuté plus haut:
    S_c%3 = (S_a + S_b)%3 = (S_a%3 + S_b%3)%3           (1)

        N'importe quel entier auquel on applique mod 3 donneras un des trois
    résultats suivants 0,1 ou 2. Puisque x%3 = 0 implique que x est divisible
    par 3 et que a et b sont premiers, a%3 ou b%3 donneront toujours soit 1,
    soit 2 puisqu'il ne seront jamais divisible par 3, excepté, bien entendu,
    dans l'unique cas où a ou b vaudrait 3. Ignorant ce cas particulier, on
    s'interesse maintenant à ce qui se passe quand on considère que S_a et S_b
    seront toujours soit 1 ou 2 et qu'on l'applique à l'équation (1). Dans le
    cas où S_a%3 = 1 et S_b%2 on a que

                            S_c%3 = (1 + 2)%3 = 0

    et que donc c n'est pas premier.
    (On se rapelle que S_c%3 = 0 --> c%3 = 0)

     On arrive évidemment à la même conclusion en interchangeant les valeurs de
     a et b. Dans les deux cas restant (a%3 = b%3) on trouve que S_c%3 \neq 0 et
     donc que c n'est pas un multiple de 3. On arrive donc à la conclusion que
     les S_a%3 et S_b%3 doivent nécessairement êtres égaux entres-eux pour que a
     et b puissent faire partie du même groupe car si ce n'est pas la cas, l'
     opération concatenate générera un multiple de 3. On se rapelle maintenant
     que 0 est aussi un possiblité et on trouve facilement que le nombre 3 ne
     pose selon ce test aucun problème à un groupe car 0 + 1 \neq 0 et 0 + 2
     \neq 0 et 0 + 0 n'arriveras jamais car on ne peut pas avoir le nombre 3
     plus d'une fois dans un seul et même groupe


'''
