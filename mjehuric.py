arr = input().split()
arr = [int(x) for x in arr]

while not all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
    if arr[0] > arr[1]:
        arr[0], arr[1] = arr[1], arr[0]
        holder = [str(x) for x in arr]
        print(' '.join(holder))
    if arr[1] > arr[2]:
        arr[1], arr[2] = arr[2], arr[1]
        holder = [str(x) for x in arr]
        print(' '.join(holder))
    if arr[2] > arr[3]:
        arr[2], arr[3] = arr[3], arr[2]
        holder = [str(x) for x in arr]
        print(' '.join(holder))
    if arr[3] > arr[4]:
        arr[3], arr[4] = arr[4], arr[3]
        holder = [str(x) for x in arr]
        print(' '.join(holder))
