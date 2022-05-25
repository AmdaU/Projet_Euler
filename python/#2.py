n,m,p,tot = 0,1,0,0

while p <= 4000000:
    p = n+m
    n = m
    m = p
    if(p%2 == 0):
        tot += p

print(tot)
