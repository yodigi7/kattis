while True:
    lastDot = input("lastDot")
    gameList = input("checking")
    if ord(lastDot) < ord(gameList) and ((not(gameList.isupper()) and not(lastDot.isupper()))or (lastDot.isupper() and gameList.isupper())):
        print("Swapped less than")
    if gameList.isupper() and not(lastDot.isupper()):
        print("Swapped is upper")
