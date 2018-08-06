done = False
points = {}
solved = []
while not done:
    try:
        info = input().split()
        time = int(info[0])
        letter = info[1]
        foundSol = False
        if info[2] == "right":
            foundSol = True
        if foundSol:
            solved.append(letter)
            try:
                points[letter] += time
            except:
                points[letter] = time
        else:
            try:
                points[letter] += 20
            except:
                points[letter] = 20        
    except:
        done = True


score = 0
numSolved = 0
for i in solved:
    score += points[i]
    numSolved += 1
print(str(numSolved) + " " + str(score))
