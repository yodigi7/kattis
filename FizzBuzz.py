theInput = input().split()
num1 = int(theInput[0])
num2 = int(theInput[1])
num3 = int(theInput[2])

for i in range(1, num3+1):
    answer = ''
    if i % num1 == 0:
        answer += "Fizz"
    if i % num2 == 0:
        answer += "Buzz"
    if i % num2 != 0 and i % num1 != 0:
        answer = i
    print(answer)
