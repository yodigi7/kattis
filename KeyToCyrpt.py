def subLetters(first, second):
    ans = ord(first) - ord(second)
    ans += 65
    if ans < 65:
        ans += 26
    return chr(ans)

cryptMess = input()
key = input()
message = ""

for i in range(min(len(cryptMess), len(key))):
    message += subLetters(cryptMess[i], key[i])

if len(key) <= len(cryptMess): 
    for i in range(len(key), len(cryptMess)):
        message += subLetters(cryptMess[i], message[i-len(key)])

print(message)
