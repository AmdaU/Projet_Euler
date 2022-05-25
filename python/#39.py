from collections import Counter
import numpy as np
from progressbar import ProgressBar

ps = []

for a in range(1,500):
    for b in range(1,a+1):
        c = np.sqrt(a**2+b**2)
        ps.append(a+b+c)

for i in ps:
    if(i > 1000):
        ps.remove(i)

print(Counter(ps).most_common(1)[0][0])


# %%
#2nd method, they both slow anyway :(

pbar = ProgressBar().start()

hiscore = 0

betest = 0

for p in range(3,1001):
    pbar.update((p/1001)**2*100)
    score = 0
    for a in range(1,p-1):
        for b in range(1,p-a):
            if(a**2 + b**2 == (p-a-b)**2):
                score += 1
    if(score > hiscore):
        hiscore = score
        betest = p

pbar.finish()

print(betest)
