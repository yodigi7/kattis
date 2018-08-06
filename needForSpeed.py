info = input().split()
info = [int(x) for x in info]
totalTime = info[1]
constant = 0
coeff = 0
for i in range(info[0]):
    holder = input().split()
    holder = [int(x) for x in holder]
    constant += holder[0]*holder[1]
    coeff += holder[0]

print((totalTime-constant)/coeff)