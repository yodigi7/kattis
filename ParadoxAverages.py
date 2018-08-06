def toInt(listH):
    for i in range(0, len(listH)):
        listH[i] = int(listH[i])
    return listH

def avg(list):
    numbers = 0
    sum = 0
    for i in list:
        sum += i
        numbers += 1
    return sum/float(numbers)

def solveCase():
    done = False
    iterator = 0
    counter = 0
    blank = input()
    numStudents = input().split()
    csList = input().split()
    ecoList = input().split()

    #Convert lists to integers
    csList = toInt(csList)
    ecoList = toInt(ecoList)
    #Sort list
    csList.sort()
    prevCSAvg = avg(csList)
    prevEcoAvg = avg(ecoList)
    while not done:
        ecoList.append(csList[0])
        csList = csList[1:]
        currentCSAvg = avg(csList)
        currentEcoAvg = avg(ecoList)
        if currentCSAvg > prevCSAvg and currentEcoAvg > prevEcoAvg:
            counter += 1
        if iterator == len(csList):
            done = True
        csList.append(ecoList[len(ecoList)-1])
        del ecoList[-1]
        if counter == len(csList):
            break
        iterator += 1
    print(counter)

numCases = int(input())

for i in range(0, numCases):
    solveCase()
