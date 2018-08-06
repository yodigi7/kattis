numStars = int(input())
print("{}:".format(numStars))
for i in range(2,numStars):
    if numStars % (i-.5) == 0 or (numStars+i-1) % (i-.5) ==  0:
        print("{},{}".format(i, i-1))
    if numStars % i == 0:
        print("{},{}".format(i, i))
