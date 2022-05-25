import numpy as np

side = 1001

spiral = np.zeros((side,side))

pos = [round(side/2),round(side/2)]

#axis,direction,length and length tracker
a,d,l,r = 1,1,1,1
for i in range(side**2):
    spiral[pos[0]][pos[1]] = i+1
    pos[a]+=d
    r-=1
    if(r == 0):
        a = (a + 1)%2
        if(a == 1):
            d *= -1
            l += 1
        r = l

int(sum([spiral[i][i] + spiral[i][side-i-1] for i in range(side)]))
