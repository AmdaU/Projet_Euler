s = ""
n = 0
while(len(s) <= 1000000):
    s += str(n)
    n += 1

prod = 1
for x in range(7):
    prod *= int(s[10**x])

print(prod)
