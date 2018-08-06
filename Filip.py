def reverse(num):
    num = str(num)
    return int(num[2]+num[1]+num[0])

info = input().split()
print(max(reverse(info[0]), reverse(info[1])))
