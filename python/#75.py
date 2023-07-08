# si d = 2 :s(s+t) < 1.5e6 ==>

from time import time
start_time = time()

def MCD(a,b):
    while b != 0:
        a, b = b, a % b
    return a


N = int(1.5e6)

_dict = dict(zip(range(1, N+1), [0]*N))
total = 0


for s in range(2,int(N**0.5)):
    for t in range(1,s):
        if MCD(s,t) == 1:
            d = 1+ (1 + s + t) % 2
            p = 2//d * s*(s+t)
            for i in range(1, N//p+1):
                l = p * i
                _dict[l] += 1

for i in _dict.values():
    if i == 2:
        total+=1

print(total)

print(time()-start_time)

