from collections import Counter

found = False

x = 1

while not found:
    found = True
    for i in range(2,7):
        if Counter(str(x)) != Counter(str(x*i)):
            found = False
    if(found):
        print(x)
    x += 1
