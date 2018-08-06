cases = int(input())
for i in range(0, cases):
    binary = bin(int(input()))
    numOnes = 0
    for j in range(0, len(binary)):
        if binary[j] == '1':
            numOnes += 1
    print(numOnes)
