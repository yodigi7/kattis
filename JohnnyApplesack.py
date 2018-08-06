from math import ceil

def advOneKilo(numApples, sackSize):
    return numApples - ceil(float(numApples)/sackSize)

numbers = input().split()
apples = int(numbers[0])
sackSize = int(numbers[1])
mile = 0

while apples > 0:
    apples = advOneKilo(apples, sackSize)
    mile += 1
mile += 1
print(mile)
