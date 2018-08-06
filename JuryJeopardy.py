def outputMaze(maze):
    for i in maze:
        holder = ''
        for j in i:
            holder += j
        print(holder)
        holder = ''

def addBot(array):
    width, height = getWidthHeight(array)
    row = []
    answer = []
    answer.append(row)
    for i in array:
        answer.append(i)
    for i in range(0, width):
        row.append('#')
    return answer

def addTop(array):
    width, height = getWidthHeight(array)
    row = []
    answer = []
    for i in range(0, width):
        row.append('#')
    answer.append(row)
    for i in array:
        answer.append(i)
    return answer

def addRight(array):
    width, height = getWidthHeight(array)
    answer = []
    row = []
    for i in range(0, height):
        for j in array[i]:
            row.append(j)
        row.append('#')
        answer.append(row)
    return answer

def addLeft(array):
    width, height = getWidthHeight(array)
    answer = []
    row = []
    for i in range(0, height):
        row.append('#')
        for j in array[i]:
            row.append(j)
        answer.append(row)
    return answer

def getWidthHeight(maze):
    height = len(maze)
    width = len(maze[0])
    return width, height

def getAddXY(direct, facing):
    addX = addY = 0
    if (facing == "right" and direct == 'F') or (facing == 'up' and direct == 'R') or (facing == 'left' and direct == 'B') or (facing == 'down' and direct == 'L'):
        addX = 1
    elif (facing == "right" and direct == 'L') or (facing == 'up' and direct == 'F') or (facing == 'left' and direct == 'R') or (facing == 'down' and direct == 'B'):
        addY = -1
    elif (facing == "right" and direct == 'B') or (facing == 'up' and direct == 'L') or (facing == 'left' and direct == 'F') or (facing == 'down' and direct == 'R'):
        addX = -1
    elif (facing == "right" and direct == 'R') or (facing == 'up' and direct == 'B') or (facing == 'left' and direct == 'L') or (facing == 'down' and direct == 'F'):
        addY = 1
    return addX, addY

def goToward(direct, x, y, facing, maze):
    addX, addY = getAddXY(direct, facing)
    width, height = getWidthHeight(maze)
    if addX == 1 and x == width-1:
        maze = addRight(maze)
    elif addY == 1 and y == height-1:
        maze = addBot(maze)
    elif (addX == -1 and x == 0) or (addX == -1 and x == 1 and (x != entX or y != entY)):
        maze = addLeft(maze)
        x += 1
    elif addY == -1 and y == 1:
        maze = addTop(maze)
        y += 1
    outputMaze(maze)
    maze[x][y] = '.'
    return addX+x, addY+y, facing, maze
    
global entX
global entY
numCases = int(input())

for i in range(0, numCases):

    entX = 0
    entY = 1
    maze = []
    hashes = ['#','#','#']
    midHashes = ['.','#','#']
    maze.append(hashes)
    maze.append(midHashes)
    maze.append(hashes)
    outputMaze(maze)
    currX = 0
    currY = 1
    width = height = 3
    facing = 'left'
    
    directions = list(input())
    for j in directions:
        holder = goToward(j, currX, currY, facing, maze)
        maze = holder[3]
        currX = holder[0]
        currY = holder[1]
        facing = holder[2]
    
