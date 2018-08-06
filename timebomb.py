def asciiToNum(arr):
    #0, 2, 3, 5, 6, 7, 8, 9
    if arr[0] == ["*", "*", "*"]:
        #0, 8, 9
        if arr[1] == ["*", " ", "*"]:
            if arr[2] == ["*", " ", "*"] and arr[3] == ["*", " ", "*"] and arr[4] == ["*", "*", "*"]:
                return 0
            elif arr[2] == ["*", "*", "*"] and arr[3] == ["*", " ", "*"] and arr[4] == ["*", "*", "*"]:
                return 8
            elif arr[2] == ["*", "*", "*"] and arr[3] == [" ", " ", "*"] and arr[4] == ["*", "*", "*"]:
                return 9
            else:
                return -1
        #2, 3, 7
        elif arr[1] == [" ", " ", "*"]:
            if arr[2] == ["*", "*", "*"] and arr[3] == ["*", " ", " "] and arr[4] == ["*", "*", "*"]:
                return 2
            elif arr[2] == ["*", "*", "*"] and arr[3] == [" ", " ", "*"] and arr[4] == ["*", "*", "*"]:
                return 3
            elif arr[2] == [" ", " ", "*"] and arr[3] == [" ", " ", "*"] and arr[4] == [" ", " ", "*"]:
                return 7
            else:
                return -1
        #5, 6
        elif arr[1] == ["*", " ", " "]:
            if arr[2] == ["*", "*", "*"] and arr[3] == [" ", " ", "*"] and arr[4] == ["*", "*", "*"]:
                return 5
            elif arr[2] == ["*", "*", "*"] and arr[3] == ["*", " ", "*"] and arr[4] == ["*", "*", "*"]:
                return 6
            else:
                return -1
        else:
            return -1
    #4
    elif arr[0] == ["*", " ", "*"] and arr[1] == ["*", " ", "*"] and arr[2] == ["*", "*", "*"] and arr[3] == [" ", " ", "*"] and arr[4] == [" ", " ", "*"]:
        return 4
    #1
    elif arr[0] == [" ", " ", "*"] and arr[1] == [" ", " ", "*"] and arr[2] == [" ", " ", "*"] and arr[3] == [" ", " ", "*"] and arr[4] == [" ", " ", "*"]:
        return 1
    return -1

arr = []
for i in range(5):
    holder = list(input())
    holder2 = []
    for i in range(0, len(holder)):
        if not (i+1)%4 == 0:
            holder2.append(holder[i])
    arr.append(holder2)

nums = len(arr[0])//3

numList = []

for a in range(nums):
    numbers = []
    for i in range(5):
        line = []
        for j in range(a*3, (a*3)+3):
            line.append(arr[i][j])
        numbers.append(line)
    numList.append(asciiToNum(numbers))

done = False
for i in numList:
    if i == -1:
        print("BOOM!!")
        done = True

if not done:
    numList = [str(x) for x in numList]
    numList = "".join(numList)
    numList = int(numList)
    if numList % 6 == 0:
        print("BEER!!")
    else:
        print("BOOM!!")