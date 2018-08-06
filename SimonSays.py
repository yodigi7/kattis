numTimes = int(input())
for i in range(0, numTimes):
    saying = input().split()
    try:
        if saying[0] == "simon" and saying[1] == "says":
            answer = ""
            for j in range(2, len(saying)):
                answer += saying[j]
                if(j<len(saying)-1):
                    answer += " "
            print(answer)
        else:
            print()
    except:
        print()
