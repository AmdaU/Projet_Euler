n,m,o,i = 1,1,0,2

while(len(str(o))<1000):
    o = m+n
    n = m
    m = o
    i += 1
i
