class Person():
    def __init__(self, num):
        self.wants = []
        self.partner = None
        self.addWant(num)

    def foundPart(self):
        if self.partner == None:
            return False
        return True

    def getPart(self):
        return self.partner

    def addWant(self, num):
        self.wants.append(num)

    def doesWant(self, num):
        for i in self.wants:
            if num == i:
                return True
        return False

    def show(self):
        print(self.wants)

def listToInt(myList):
    for i in range(0, len(myList)):
        myList[i] = int(myList[i])
    return myList

def findValidLoop(startPoint, peopleLeft, people, peopleNum):
    possibilities = []
    for i in people[peopleNum[startPoint]].wants:
        

info = listToInt(input().split())
people = {}
done = False
peopleNum = []

for i in range(0,info[1]):
    line = listToInt(input().split())
    if line[0] in people:
        people[line[0]].addWant(line[1])
    else:
        people[line[0]] = Person(line[1])
        peopleNum.append(line[0])

startPoint = 0
while done == False:
    peopleLeft = peopleNum
    innerDone = True
    while innerDone == False:
        
    
    startPoint += 1
    if startPoint > len(peopleNum):
        done = True
        break

for i in people:
    people[i].show()
