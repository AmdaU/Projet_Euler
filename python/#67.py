with open("triangle.txt") as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]

triangle = []

for line in lines:
    numb = []
    n = 0
    while(n<len(line)):
        numb.append(int(line[n:n+2]))
        n +=3
    triangle.append(numb)

for i in range(len(triangle))[-2::-1]:
    for j in range(len(triangle[i])):
        triangle[i][j] += max(triangle[i+1][j],triangle[i+1][j+1])

print(triangle[0][0])
