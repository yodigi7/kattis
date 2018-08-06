import math

def findDiam(vol):
    return ((vol/math.pi)**(1/3))*2

def cylVol(diam):
    return (((diam/2)**3)*math.pi)

##info = input().split()
##info = [float(x) for x in info]
##while not (info[0] == float(0) and info[1] == float(0)):
##    print(findDiam(cylVol(info[0])-info[1]))
##    info = input().split()
##    info = [float(x) for x in info]

while True:
    diam1 = float(input())
    diam2 = float(input())
    print(cylVol(diam1))
    print(cylVol(diam2))
    print(cylVol(diam1)-cylVol(diam2))
