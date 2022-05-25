sfrom numpy import ceil

isSq = lambda n: n == round(n**(1/2))**2

D = 2

lst = []
while D < 61:
    g = 1
    if isSq(D):
        D+=1
    found = False
    y = 1
    q = 1
    while not found:
        a = D**(1/2)*y
        if round(a+0.5) < a + g:
            q += 1
            b = D*y**2 + 1
            if isSq(b):
                found = True
                lst.append(b*(1/2))
                print(b**(1/2))

        print(y,q,g)
        x = (1 + D*(y-1000000)**2)**(1/2)
        g = x - (x**2 - 1)**(1/2)
        y+=1

    D +=1
