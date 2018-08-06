numNames = int(input())
setNum = 1
while not numNames == 0:
    nameArr = []
    print("SET " + str(setNum))
    for i in range(numNames):
        nameArr.append(input())
    for i in range(0, len(nameArr), 2):
        print(nameArr[i])
    for i in reversed(range(1, len(nameArr), 2)):
        print(nameArr[i])
    numNames = int(input())
    setNum += 1