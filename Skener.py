info = input().split()
info = [ int(x) for x in info ]

originalPic = []
for i in range(info[0]):
    holder = list(input())
    for j in range(info[2]):
        line = ''
        for k in range(info[1]):
            char = ''
            for l in range(info[3]):
                char += holder[k]
            line += char
        print(line)