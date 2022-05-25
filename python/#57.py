num,count = (3,2),0

for i in range(1,1001):
    if len(str(num[0])) > len(str(num[1])):
        count += 1
    num =(2*num[1]+num[0],sum(num))
count
