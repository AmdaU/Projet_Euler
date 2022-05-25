def cycleLenght(d,l):
    while 1:
        if l[-1]%d*10 in l:
            return len(l) - l.index(l[-1]%d*10)
        l.append(l[-1]%d*10)

max([cycleLenght(i,[1]),i] for i in range(1,1000))[1]
