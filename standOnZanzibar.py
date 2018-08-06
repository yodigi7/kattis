def leastImported(prev, now):
    holder = prev*2
    if holder >= now:
        return 0
    else:
        return now - holder

cases = int(input())
for i in range(cases):
    info = input().split()
    info = [int(x) for x in info]
    imported = 0
    for i in range(len(info)):
        if not info[i+1] == 0:
            imported += leastImported(info[i], info[i+1])
        else:
            break
    print(imported)
