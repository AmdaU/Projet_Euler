matrix = []
with open('matrix.txt') as file:
    for line in file.readlines():
        matrix.append(eval(f'[{line.strip()}]'))


transp = list(zip(*matrix))


for col in transp[:-1][::-1]:
    for elem in col:


print(transp)
