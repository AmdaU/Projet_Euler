def MCD(a,b):
    while b != 0:
        a, b = b, a % b
    return a

low_score, scorer, d = 1, 7, 1
while (d:=d+1) < int(1e6):
    if d !=7:
        n = int(d*3/7)
        if (MCD(n,d)==1) and (score := (3/7-n/d)) < low_score:
                low_score, scorer = score, n

print(scorer)
