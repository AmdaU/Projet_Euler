fact = lambda x: x*fact(x-1) if x>1 else 1
sum(map(int,str(fact(100))))
