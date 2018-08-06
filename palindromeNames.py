def pivotScore(name, pivot):
    odd = False
    length = len(name) - pivot
    length = min(pivot+1, length)
    maxi = 0
    #Try for an odd-character name
    currScore = 1
    print(length)
    for i in range(1, length):
        if name[pivot-i] == name[pivot+i]:
            currScore += 2
            print(name[pivot-i])
        else:
            currScore += 1
    if maxi < currScore:
        odd = True
    maxi = max(maxi, currScore)

    length = len(name) - (pivot+1)
    length = min(pivot+1, length)
    #Try even-character name
    currScore = 0
    for i in range(0, length):
        if name[pivot-i] == name[pivot+i+1]:
            currScore += 2
        else:
            currScore += 1
    if maxi < currScore:
        odd = True
    maxi = max(maxi, currScore)    
    return maxi, odd

def tryAllPivots(name):
    maxScore = 0
    for i in range(len(name)):
        holder = list(pivotScore(name, i))
        if holder[0] > maxScore:
            print(holder[0], maxScore)
            maxScore = holder[0]
    return len(name) - maxScore

name = input()
print(tryAllPivots(name))
