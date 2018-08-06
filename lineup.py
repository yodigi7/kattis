numNames = int(input())
incr = False
name1 = input()
name2 = input()
if not name1 > name2:
    incr = True

for i in range(numNames-2):
    name1 = name2
    name2 = input()
    length = len(name1)
    min(length, len(name2))
    name1 = name1[:length]
    name2 = name2[:length]
    if (not incr) and name2 > name1:
        print('NEITHER')
        break
    elif incr and name1 > name2:
        print('NEITHER')
        break
else:
    if incr:
        print('INCREASING')
    else:
        print('DECREASING')
