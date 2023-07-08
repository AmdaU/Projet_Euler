from functools import lru_cache

@lru_cache(maxsize=2**20)
def p(n):
    if n < 2:
        return 1
    k, total = 1, 0
    while (g_k:=(3*k**2 -k)//2) <= n:
        total += ((-1)**((k-1)%2)* p(n-g_k))
        if (k:=k*-1) > 0:
            k+=1

    return total % 1000000

i = 0
while p(i:=i+1):
    pass

print(i)
