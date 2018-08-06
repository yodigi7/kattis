inp = input()

myL = inp.split('-')
answer = ''
for i in range(0,len(myL)):
    answer += myL[i][0]
print(answer)
