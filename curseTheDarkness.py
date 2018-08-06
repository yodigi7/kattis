from math import sqrt

def getDistance(bookArr, candleArr):
    return sqrt(((bookArr[0]-candleArr[0])**2)+((bookArr[1]-candleArr[1])**2))

testCases = int(input())
for i in range(0, testCases):
    curse = True
    bookXY = input().split()
    bookXY = [float(x) for x in bookXY]
    numCandles = int(input())
    for j in range(0, numCandles):
        candle = input().split()
        candle = [float(x) for x in candle]
        if getDistance(bookXY, candle) < 8:
            curse = False
            break
    if curse == True:
        print("curse the darkness")
    else:
        print("light a candle")
