from collections import Counter
from time import time


time_start = time()

ps = []

for a in range(1,500):
    for b in range(1,a+1):
        c = (a**2+b**2)**(1/2)
        ps.append(a+b+c)

for i in ps:
    if(i > 1000):
        ps.remove(i)

print(Counter(ps).most_common(1)[0][0])
print(time()-time_start)

# 2nd method, they both slow anyway :(

time_start = time()

hiscore = 0

betest = 0

for p in range(2,1001):
    score = 0
    for a in range(1,(p-1)//2):
        for b in range(1,(p-a)//2):
            if(a**2 + b**2 == (p-a-b)**2):
                score += 1
    if(score > hiscore):
        hiscore = score
        betest = p

print(betest)

print(time()-time_start)
