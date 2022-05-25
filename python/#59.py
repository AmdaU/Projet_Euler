with open("decryption.txt") as f: exec('nums = ['+ f.readline()+']')

Decoded, letters = False, [96,97,97]

while not Decoded:
    letters[0] +=1
    for i in [0,1]:
        if letters[i]>122:
            letters[i] = 97
            letters[i+1] += 1

    decy=list(map(lambda x: x[0]^x[1],list(zip(letters*(len(nums)//3), nums))))
    i = 0
    while i<len(decy)-5 and not Decoded:
        if decy[i: i+5] == [32,116,104,101,32] : Decoded = True
        i+=1

print("".join(list(map(chr,decy))))
sum(decy)
