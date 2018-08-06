magic = lambda nums: int(''.join(str(i) for i in nums))

def dec2BinRev(num):
    answer = []
    while(num != 0):
        answer.insert(0, num%2)
        num //= 2
    answer = reversed(answer)
    return magic(answer)

number = int(input())
print(int(str(dec2BinRev(number)), 2))
