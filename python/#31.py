def partition(a,quantites):
    numberOfWays = 0
    for i in quantites:
        left = a - i
        if left > 0:
            numberOfWays += partition(left,quantites[quantites.index(i):])
        elif left == 0:
            return numberOfWays+1
        else:
            return numberOfWays

partition(200,[1,2,5,10,20,50,100,200])
