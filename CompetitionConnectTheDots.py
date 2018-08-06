def findCoorOfChar(gameList, char):
    for i in range(0, len(gameList)):
        for j in range(0, len(gameList[i])):
            if gameList[i][j] == char:
                return i, j

def dirOfNextPointList(gameList):
    startI = startJ = 0
    ansList = []
    currChar = '0'
    lastDot = findLastDot(gameList)
    while currChar != lastDot:
        nextChar = next[currChar]
        currCharCoor = findCoorOfChar(gameList, currChar)
        nextCharCoor = findCoorOfChar(gameList, nextChar)
        if currCharCoor[0] > nextCharCoor[0]:
            ansList.append("up")
        elif currCharCoor[0] < nextCharCoor[0]:
            ansList.append("down")
        elif currCharCoor[1] > nextCharCoor[1]:
            ansList.append("left")
        elif currCharCoor[1] < nextCharCoor[1]:
            ansList.append("right")
        currChar = nextChar
    return ansList
        

def findLastDot(gameList):
    dotsOnBoard = []
    lastDot = None
    #Find last point on board
    for i in range(0, len(gameList)):
        for j in range(0, len(gameList[i])):
            if gameList[i][j] != '.':
                dotsOnBoard.append(gameList[i][j])
                if lastDot == None:
                    lastDot = gameList[i][j]
                elif ord(lastDot) < ord(gameList[i][j]) and ((gameList[i][j] != '|' and gameList[i][j] != '-' and gameList[i][j] != '+') and (not(gameList[i][j].isupper()) and not(lastDot.isupper()))or (lastDot.isupper() and gameList[i][j].isupper())):
                    lastDot = gameList[i][j]
                if gameList[i][j].isupper() and not(lastDot.isupper()):
                    lastDot = gameList[i][j]
    return lastDot

def solveGame(gameList):
    dirList = dirOfNextPointList(gameList)
    counter = 0
    lastDot = findLastDot(gameList)
    char = '0'
    while char != lastDot:
        currCoor = []
        currCoor.append(findCoorOfChar(gameList, char)[0])
        currCoor.append(findCoorOfChar(gameList, char)[1])
        nextChar = next[char]
        direction = dirList[counter]
        while gameList[currCoor[0]][currCoor[1]] != nextChar:
            if direction == "up":
                currCoor[0] -= 1
            elif direction == "down":
                currCoor[0] += 1
            elif direction == "right":
                currCoor[1] += 1
            elif direction == "left":
                currCoor[1] -= 1
            if gameList[currCoor[0]][currCoor[1]] == '.' and (direction == "up" or direction == "down"):
                gameList[currCoor[0]][currCoor[1]] = '|'
            elif gameList[currCoor[0]][currCoor[1]] == '.' and (direction == "left" or direction == "right"):
                gameList[currCoor[0]][currCoor[1]] = '-'
            elif (gameList[currCoor[0]][currCoor[1]] == '|' and (direction == "left" or direction == "right")) or (gameList[currCoor[0]][currCoor[1]] == '-' and (direction == "up" or direction == "down")):
                gameList[currCoor[0]][currCoor[1]] = '+'
        char = next[char]
        counter += 1
    return gameList
    
end = False
gamesHold = []
games = []
string = ''
while not end:
    #Try to get a new line if possible
    currLine = ' '
    try:
        currLine = input()
    except EOFError:
        end = True
    gamesHold.append(repr(currLine))

holder = []
for i in range(0, len(gamesHold)):
    if gamesHold[i] == "''" or gamesHold[i]=="' '":
        games.append(holder)
        holder = []
    else:
        gamesHold[i] = gamesHold[i].replace("'", "")
        holder.append(list(gamesHold[i]))


next = {}
for i in range(0,9):
    next[str(i)] = str(i+1)
next['9'] = 'a'
next['z'] = 'A'
for i in range(0, 25):
    next[chr(ord('a')+i)] = chr(ord('b')+i)
    next[chr(ord('A')+i)] = chr(ord('B')+i)

for i in range(0, len(games)):
    answer = solveGame(games[i])
    for j in range(0, len(answer)):
        print("".join(answer[j]))
    if i+1 != len(games):
        print()
