def getWidth(line):
    answer = 0
    for i in range(1, len(line)):
        answer += int(line[i])
    return answer

def decodeLine(line):
    answer = ''
    currChar = line[0]
    #Go through each number
    for i in range(1, len(line)):
        #Add the characters
        for j in range(0, int(line[i])):
            answer += currChar
        if currChar == '#':
            currChar = '.'
        else:
            currChar = '#'
    return answer
    

def decodeImg(first):
    error = False
    numLines = int(input())
    answer = []
    corrWidth = 0
    if(numLines == 0):
        return True, error
    if not first:
        print()
    for i in range(0, numLines):
        currLine = input().split()
        if i == 0:
            corrWidth = getWidth(currLine)
        elif corrWidth != getWidth(currLine):
            error = True
        answer.append(decodeLine(currLine))
    for i in range(0, len(answer)):
        print(answer[i])
    #Not done
    return False, error

done = False
first = True
while not done:
    done, error = decodeImg(first)
    first = False
    if error:
        print("Error decoding image")
