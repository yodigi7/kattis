info = input().split()
numCases = int(info[0])
T = int(info[1])
finished = remainingTime = 0
info = input().split()
info = [int(x) for x in info]
for i in range(numCases):
    if remainingTime + info[i] <= T:
        remainingTime += info[i]
        finished += 1
    else:
        break
print(finished)
