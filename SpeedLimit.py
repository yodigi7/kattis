import sys
numTrials = 1
while 1==1:
    answer = 0
    previous = 0
    numTrials = int(input())
    if numTrials <= 0:
        break;
    while numTrials > 0:
        mph, time = input().split()
        answer += (int(time) - previous)*int(mph)
        previous = int(time)
        numTrials -= 1
    print(str(answer) + " miles")
    
