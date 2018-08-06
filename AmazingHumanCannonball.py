import math
cases = int(input())
for i in range(cases):
    vel, theta, x, h1, h2 = input().split()
    vel, theta, x, h1, h2 = float(vel), float(theta), float(x), float(h1), float(h2)
    t = x/(vel*math.cos(math.radians(theta)))
    y = (vel*t*math.sin(math.radians(theta)))-(.5*9.81*t*t)
    if y-1 > h1 and y+1 < h2:
        print("Safe")
    else:
        print("Not Safe")
