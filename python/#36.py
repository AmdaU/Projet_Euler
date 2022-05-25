def toBin(x):
    digits = []
    puiss = 0
    while(x/2 >= 2**puiss):
        puiss +=1
    for i in range(puiss,-1,-1):
        if(x - 2**i >= 0):
            digits.append(1)
            x -= 2**i
        else:
            digits.append(0)
    return digits

somme = 0

for i in range(1,1000000):
    b10 = str(i)
    b2 = toBin(i)
    if(b10 == b10[::-1] and b2 == b2[::-1]):
        somme += i

somme
