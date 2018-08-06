totalCost = 0
cost = float(input())
numLawns = int(input())
for i in range(0, numLawns):
    info = input().split()
    width = float(info[0])
    height = float(info[1])
    totalCost += width*height*cost
print('{0:.7f}'.format(totalCost))
