info = input().split()
info = [int(x) for x in info]
extra = info[1]-info[0]
answer = ''
if extra < 0:
    extra *= -1
    answer += "Dr. Chaz needs " + str(extra) + " more piece"
    if not extra == 1:
        answer += 's'
    answer += " of chicken!"
else:
    answer += "Dr. Chaz will have " + str(extra) + " piece"
    if not extra == 1:
        answer += 's'
    answer += " of chicken left over!"
print(answer)