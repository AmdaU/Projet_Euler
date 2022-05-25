l, k, mm = [2,1], 2, lambda l: 1 if not l else l.pop()*mm(l)

for i in range(33):
    l+=[k,1,1]
    k+=2

a, b, c = l.pop(0), 1, l.pop(0)

while len(l) > 0:
    a, b, c = c*a+b, a, l.pop(0)

sum(map(int,str(a)))
