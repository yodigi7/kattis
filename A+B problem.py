numbers = input()
numbers = input().split()

numbers = [int(x) for x in numbers]

counter = 0

numbersLen = len(numbers)

for i in range(0, numbersLen):
    for j in range(0, numbersLen):
        for k in range(0, numbersLen):
            if i == j or j == k or i == k:
                pass
            elif numbers[i] + numbers[j] == numbers[k]:
                counter += 1
print(counter)
