with open("names.txt") as f:
    names = f.readline().replace('"','').split(",")
f.close()

dic = dict(zip('"ABCDEFGHIJKLMNOPQRSTUVWXYZ',range(27)))

names.sort()

sum([sum([dic[car]*(i+1) for car in names[i]]) for i in range(len(names))])
