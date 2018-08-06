domValue = [11, 4, 3, 20, 10, 14, 0, 0]
nonDomVal = [11, 4, 3, 2, 10, 0, 0, 0]

def findValue(num, suit):
    if suit == domSuit:
        return domValue[numConv[num]]
    else:
        return nonDomVal[numConv[num]]

answer = 0
firstInput = input().split()
numHands = int(firstInput[0])
domSuit = firstInput[1]
numConv = dict()
numConv['A'] = 0
numConv['K'] = 1
numConv['Q'] = 2
numConv['J'] = 3
numConv['T'] = 4
numConv['9'] = 5
numConv['8'] = 6
numConv['7'] = 7

for i in range(0, 4*numHands):
    card = list(input())
    num = card[0]
    suit = card[1]
    answer += findValue(num, suit)

print(answer)
