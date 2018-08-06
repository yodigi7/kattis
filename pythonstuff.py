import sys

seen = []
answer1 = []
answer2 = []
for i in range(0,3):
        num1, num2 = input().split()
        num1 = int(num1)
        num2 = int(num2)
        answer1.append(num1)
        answer2.append(num2)
for number in answer1:
    if number in seen:
        answer1.remove(number)
        answer1.remove(number)
    else:
        seen.append(number)
seen = []
for number in answer2:
    if number in seen:
        answer2.remove(number)
        answer2.remove(number)
    else:
        seen.append(number)
print (str(answer1[0]) + " " + str(answer2[0]))
