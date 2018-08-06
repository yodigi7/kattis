import sys
numTemps = int(input())
answer = 0
numbers = input().split()
for number in numbers:
    if int(number) < 0:
        answer += 1
print (answer)
