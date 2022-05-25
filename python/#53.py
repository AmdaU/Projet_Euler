from scipy.special import comb

sum([1 for n in range(1,101) for r in range(0,n) if comb(n, r, exact=False, repetition=False) > 1000000])
