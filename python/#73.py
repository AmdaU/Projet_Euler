from math import ceil

def MCD(a,b):
    while b != 0:
        a, b = b, a % b
    return a

s = 0
for d in range(4,12000+1):
    for n in range(int(ceil(d/3)), (d//2)+1):
        s += (MCD(d,n) == 1)

print(s)

