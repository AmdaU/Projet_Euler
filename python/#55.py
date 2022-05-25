count = 0
for x in range(10000):
    itts,n = 0, x + int(str(x)[::-1])
    while str(n) != str(n)[::-1]:
        itts+=1
        n += int(str(n)[::-1])
        if itts == 50:
            count +=1
            break

print(count)
