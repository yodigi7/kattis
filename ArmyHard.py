numCases = int(input())

for i in range(0, numCases):
    godArmy = input()
    godArmy = input()
    godArmy = input().split()
    mechArmy = input().split()

    godArmy = [int(x) for x in godArmy]
    mechArmy = [int(x) for x in mechArmy]

    godArmy.sort()
    mechArmy.sort()

    if mechArmy[len(mechArmy)-1] > godArmy[len(godArmy)-1]:
        print("MechaGodzilla")
    else:
        print("Godzilla")
##    
##    while len(mechArmy) != 0 and len(godArmy) != 0:
##        if mechArmy[0] > godArmy[0]:
##            number = godArmy[0]
##            for i in range(0, len(godArmy)):
##                if godArmy[0] == number:
##                    del godArmy[0]
##                else:
##                    break
##        else:
##            number = mechArmy[0]
##            for i in range(0, len(mechArmy)):
##                if mechArmy[0] == number:
##                    del mechArmy[0]
##                else:
##                    break
##
##    if len(mechArmy) == 0:
##        print("Godzilla")
##    else:
##        print("MechaGodzilla")
