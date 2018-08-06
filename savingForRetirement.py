info = input().split()
B, Br, Bs, A, As = (int(x) for x in info)
bSaveYears = Br - B
bMoney = bSaveYears*Bs

aMoney = 0
Ar = A
while aMoney <= bMoney:
    aMoney += As
    Ar += 1
print(Ar)
