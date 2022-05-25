import numpy as np

D = 0
n = 2

found = False

while(not found):
    pn1 = n*((3*n)-1)/2
    n2 = n -1
    while(not found and n2 > 0):
        pn2 = n2*(3*n2-1)/2
        s = pn1 + pn2
        d = pn1 - pn2
        if((1+np.sqrt(1+24*s))/6 == round((1+np.sqrt(1+24*s))/6) and (1+np.sqrt(1+24*d))/6 == round((1+np.sqrt(1+24*d))/6)):
            found = True
            D = int(d)
        n2 -= 1
    n += 1
print(D)
