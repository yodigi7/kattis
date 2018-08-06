def numFlies(picture, x, y, width):
    score = 0
    for i in range(y+1, y+width-1):
        for j in range(x+1, x+width-1):
            if picture[i][j] == '*':
                score += 1
    return score

#Get input
info = input().split()
info = [int(x) for x in info]
picture = []
for i in range(info[0]):
    picture.append(list(input()))

#Calculate place to swing
maxFlies = 0
for i in range(0, len(picture)-info[2]+1):
    for j in range(0, len(picture[0])-info[2]+1):
        if maxFlies < numFlies(picture, j, i, info[2]):
            maxFlies = numFlies(picture, j, i, info[2])
            maxX, maxY = j, i
print(maxFlies)

for i in range(len(picture)):
    for j in range(len(picture[0])):
        if (i == maxY and j == maxX) or (i == maxY+info[2]-1 and j == maxX) or (i == maxY+info[2]-1 and j == maxX+info[2]-1) or (i == maxY and j == maxX+info[2]-1):
            picture[i][j] = '+'
        elif (i == maxY and j < maxX+info[2]-1 and j > maxX) or (i == maxY+info[2]-1 and j < maxX+info[2]-1 and j > maxX):
            picture[i][j] = '-'
        elif (j==maxX and i > maxY and i < maxY+info[2]-1) or (j==maxX+info[2]-1 and i > maxY and i < maxY+info[2]-1):
            picture[i][j] = '|'

for i in range(len(picture)):
    line = ''
    for j in range(len(picture[0])):
        line += picture[i][j]
    print(line)