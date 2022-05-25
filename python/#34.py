fact = lambda x: x*fact(x-1) if x>1 else 1
n,somme = 3,0

while(n < len(str(n))*fact(9)):
    if(sum(fact(int(i)) for i in str(n)) == n):
        somme += n
    n+=1

somme
