with open("poker.txt") as f:
    lines = f.readlines()

games = [x.strip().split(" ") for x in lines]

trans = dict(zip(("A",*(map(str,range(2,10))),*("T","J","Q","K")),range(1,14)))

high = lambda h: max([value(c) for c in h])
values = lambda h: [trans[c[0]] for c in h]
order = lambda h: list(map(lambda x: (x-2)%14+2,h))

reps = lambda h,v: [x for x in set(values(h)) if values(h).count(x) == v]

pair = lambda h: (len(reps(h,2)),reps(h,2))
dp = lambda h: (len(reps(h,2)) == 2,reps(h,2))
three = lambda h: (len(reps(h,3)),reps(h,3))
straight = lambda h: (all((x in values(h) for x in range(high(h)-4,high(h)+1))),[high(h)])
flush = lambda h: (all([c[-1] == h[0][-1] for c in h[1:]]),[high(h)])
fh = lambda h: (len(reps(h,3)) == 1 and len(reps(h,2)) == 1,reps(h,3) + reps(h,2))
four = lambda h: (len(reps(h,4)),reps(h,4))
sf = lambda h: (flush(h)[0] and straight(h)[0], [high(h)])
rf = lambda h: (all(x in values(h) for x in [1,10,11,12,13]) and flush(h)[0],1)

ranks = [pair,dp,three,straight,flush,fh,four,sf,rf]

wins=0

for g in games:
    rank1,rank2,val1,val2 = 0,0,0,0
    for i in range(len(ranks)):
        if ranks[i](g[:5])[0]:
            rank1 = i+1
            val1 = max(order(ranks[i](g[:5])[1]))
        if ranks[i](g[5:])[0]:
            rank2 = i+1
            val2 = max(order(ranks[i](g[5:])[1]))
    if rank1 > rank2:
        wins+=1
    elif rank1 == rank2:
        if val1 > val2:
            wins +=1
        elif val1 == val2:
            vals1,vals2 = order(values(g[:5])),order(values(g[5:]))
            vals1.sort()
            vals2.sort()
            found = False
            while not found:
                val1,val2 = vals1.pop(), vals2.pop()
                if val1 > val2:
                    wins +=1
                    found = True
                elif val1 < val2:
                    found = True

print(wins)
