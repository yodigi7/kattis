def getLongestLine(img):
    longest = 0
    for i in range(0, len(img)):
        if len(img[i]) > longest:
            longest = len(img[i])
    return longest

def rotate(img):
    width = getLongestLine(img)
    height = len(img)
    longest = width
    answer = []
    if(width < height):
        longest = height
    for i in range(0, longest):
        answer.append([' '] * longest)
    for i in range(0, len(img)):
        for j in range(0, len(img[i])):
            try:
                print("Swapped at " + str(j) + " " + str(i))
                answer[j][i] = img[i][j]
            except:
                print("Entered a space")
                answer[j][i] = ' '
        print(answer[i])
        

lines = 1
while lines:
    lines = int(input())
    img = []
    for i in range(0, lines):
        line = input()
        img.append(list(line))
    rotate(img)
    print()
    
