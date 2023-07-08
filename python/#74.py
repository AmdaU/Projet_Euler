fact = lambda n: n*fact(n-1) if n > 1 else 1
link = lambda n: sum([fact(int(s)) for s in str(n)])

total = 0
for n in range(1000000):
    current_chain = [n]
    while (n:=link(n)) not in current_chain:
        current_chain.append(n)
    total += len(current_chain) == 60
