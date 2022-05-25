def estPrem(x):
    if (x <= 1):
        return False
    pasDeFacteur = True
    tested = x
    candidateForFactor = 2
    while(candidateForFactor <= tested/candidateForFactor and pasDeFacteur):
        if(tested % candidateForFactor == 0):
            pasDeFacteur = False
        candidateForFactor += 1
    return pasDeFacteur

def nextPrime(x):
    tested = x+1
    while True:
        if(estPrem(tested)):
            return tested
        tested += 1

def toBin(x,puiss):
    digits = []
    for i in range(puiss,-1,-1):
        if(x - 2**i >= 0):
            digits.append(1)
            x -= 2**i
        else:
            digits.append(0)
    return digits

def configurations(x):
    confs = []
    outs = []
    for i in range(1,2**len(x)-1):
        confs.append(toBin(i,len(x)-1))
    for i in range(len(confs)):
        outies = ""
        for j in range(len(confs[i])):
            if(confs[i][j]):
                outies += x[j]
            else:
                outies += "*"
        outs.append(outies)
    return outs

prime = 11

found = False

noice = 0

while not found:
    prime = nextPrime(prime)
    s = str(prime)
    for conf in configurations(s):
        score = 0
        for i in range(10):
            num = conf.replace("*",str(i))
            if estPrem(int(num)):
                if(num[0] == "0"):
                    score -= 1
                score += 1
                if(score == 8):
                    nha = True
                    n = 0
                    while nha:
                        if(estPrem(int(conf.replace("*",str(n)))) and conf.replace("*",str(n))[0] != 0):
                            print(int(conf.replace("*",str(n))))
                            nha = False
                        n+=1
                    found = True
