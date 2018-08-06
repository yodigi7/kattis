def length(binary):
    for i in range(len(binary)):
        if binary[i] == '1':
            return len(binary)-i
    return 0

files, maxSize = input().split()
files, maxSize = int(files), int(maxSize)

if length(bin(files))-1 > maxSize:
    print("no")
else:
    print("yes")
