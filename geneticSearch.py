def patternInSeq(patt, seq):
    counter = 0
    pattLen = len(patt)
    for i in range(len(seq)-pattLen+1):
        if patt == seq[i:i+pattLen]:
            counter += 1
    return counter

def testList(myList, seq):
    myList = list(set(myList))
    counter = 0
    for entry in myList:
        counter += patternInSeq(entry, seq)
    return counter

def type2(patt, seq):
    myList = []
    for i in range(len(patt)):
        holder = list(patt)
        del holder[i]
        myList.append(''.join(holder))
    return testList(myList, seq)

def type3(patt, seq):
    myList = []
    for i in range(0, len(patt)+1):
        for char in ['A', 'T', 'C', 'G']:
            holder = list(patt)
            holder.insert(i, char)
            myList.append(''.join(holder))
    return testList(myList, seq)

try:
    while(True):
        pattern, string = input().split()
        print(str(patternInSeq(pattern, string)) + " " + str(type2(pattern, string)) + " " + str(type3(pattern, string)))
except:
    pass
