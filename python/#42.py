import numpy as np

with open("words.txt") as f:
    lines = f.readlines()

words = str(lines[0]).split(',')
words = [x.strip('"') for x in words]

dic = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

amount = 0

for word in words:
    score = 0
    for l in word:
        score += dic[l]
    if(np.sqrt(1 + 8*score) == round(np.sqrt(1 + 8*score))):
        amount += 1

print(amount)
