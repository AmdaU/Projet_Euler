isTri = lambda x:((1+8*x)**(1/2)-1)/2 == round(((1+8*x)**(1/2)-1)/2)
isPent = lambda x:(np.sqrt(1+24*x)+1)/6 == round((np.sqrt(1+24*x)+1)/6)
n,next,found = 0,0,False

while(not found):
    h = n*(2*n-1)
    found = isTri(h) and isPent(h) and h > 40755
    if found: next = h
    n+=1

print(next)
