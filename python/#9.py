[a*b*c for c in range(500) for a in range(2,c) for b in range(1,a) if a*a + b*b == c*c and a+b+c == 1000][0]
