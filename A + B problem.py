def isSol(num1, num2, num3):
    if num1 + num2 == num3:
        return True
    return False

def getCounter(num1, num2, num3):
    counter = 2
    if isSol(num1, num3, num2):
        counter += 2
    if isSol(num2, num3, num1):
        counter += 2
    return counter

numbers = input()
numbers = input().split()

for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])

counter = 0

for i in range(0, len(numbers)-2):
    for j in range(i+1, len(numbers)-1):
        for k in range(j+1, len(numbers)):
            if isSol(numbers[i], numbers[j], numbers[k]):
                addCounter = getCounter(numbers[i], numbers[j], numbers[k])
                counter += addCounter

print(counter)
