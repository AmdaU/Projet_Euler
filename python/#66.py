from decimal import *
getcontext().prec = 100


def xn(hs, ks, xs):
    def MCD(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    hn, kn = int(xs[-1])*hs[-1] + hs[-2], int(xs[-1])*ks[-1] + ks[-2]
    hn, kn = (x//MCD(hn, kn) for x in (hn, kn))

    xs.append(1/(xs[-1]-int(xs[-1])))
    hs.append(hn)
    ks.append(kn)
    return hs[-1], ks[-1]


def satisfies_pell(x, y, D):
    return x*x - D*y*y - 1


squares = [x*x for x in range(int(1001**(1/2))+1)]

xmax, dmax = 0, 0
for D in range(2, 1001):
    if D not in squares:
        hs, ks, xs = [0, 1], [1, 0], [Decimal(D).sqrt()]
        while True:
            a, b = xn(hs, ks, xs)
            if not satisfies_pell(a, b, D):
                if a > xmax:
                    dmax, xmax = D, a
                break

print(dmax)
