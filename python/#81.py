triangle = [[] for i in range(2*80-1)]

with open('matrix.txt') as file:
    for i, line in enumerate(file):
        for j, val in enumerate(line.strip().split(',')):
            triangle[i+j].append(int(val))

for i in range(1, len(triangle)):
    diff = i - len(triangle[i])
    triangle[i] = [triangle[i][0]]*(diff//2+1) + triangle[i] + [triangle[i][-1]]*(diff//2+1)


for i in range(len(triangle))[-2::-1]:
    for j in range(len(triangle[i])):
        triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1])

print(triangle[0][0])
