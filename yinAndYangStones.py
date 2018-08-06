ring = list(input())
whites = blacks = 0
for i in ring:
    if i == 'W':
        whites += 1
    else:
        blacks += 1
if whites == blacks:
    print(1)
else:
    print(0)