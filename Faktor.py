from math import ceil
numbers = input().split()

for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])

answer = numbers[0]*numbers[1]

i=0
while ceil(float(answer)/numbers[0]) >= numbers[1]:
    answer -= 1

print(answer+1)
