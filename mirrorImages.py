cases = int(input())
for a in range(cases):
    info = input().split()
    info = [int(x) for x in info]
    storageArr = []
    answerArr = []
    for i in range(info[0]):
        storageArr.append(list(input()))
        holder = []
        for j in range(info[1]):
            holder.append('')
        answerArr.append(holder)
    for i in range(len(storageArr)):
        for j in range(len(storageArr[0])):
            answerArr[len(storageArr)-i-1][len(storageArr[0])-1-j] = storageArr[i][j]
    print("Test " + str(a+1))
    for i in range(len(answerArr)):
        line = ''
        for j in range(len(answerArr[0])):
            line += answerArr[i][j]
        print(line)