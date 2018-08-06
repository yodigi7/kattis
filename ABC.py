numbers = input().split()
for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])
order = list(input())

converter = {}
converter['C'] = max(numbers[0], numbers[1], numbers[2])
converter['A'] = min(numbers[0], numbers[1], numbers[2])
if converter['C'] != numbers[0] and converter['A'] != numbers[0]:
    converter['B'] = numbers[0]
elif converter['C'] != numbers[1] and converter['A'] != numbers[1]:
    converter['B'] = numbers[1]
elif converter['C'] != numbers[2] and converter['A'] != numbers[2]:
    converter['B'] = numbers[2]

answer = ''
for i in order:
    answer += str(converter[i]) + ' '
print(answer)
