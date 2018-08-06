def drinksOnDay(numBottles, cost):
    return numBottles//cost, numBottles%cost

info = input().split()
cost = int(info[2])
numBottles = int(info[0]) + int(info[1])
drank = 0
while numBottles >= cost:
    drankToday, numBottles = drinksOnDay(numBottles, cost)
    numBottles += drankToday
    drank += drankToday
print(drank)
