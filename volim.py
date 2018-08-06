currPerson = int(input())-1
numQuestions = int(input())
time = 0
endTime = 210
for i in range(numQuestions):
    info = input().split()
    time += int(info[0])
    if time >= endTime:
        break
    if info[1] == 'T':
        currPerson += 1
print(currPerson%8+1)