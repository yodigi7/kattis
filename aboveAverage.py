if __name__ == '__main__':
    numCases = int(input())
    for i in range(numCases):
        holder = input().split()
        numStudents = int(holder[0])
        grades = []
        for i in range(1,numStudents+1):
            grades.append(int(holder[i]))
        average = sum(grades)/float(numStudents)
        numAboveAvg = 0
        for i in grades:
            if i > average:
                numAboveAvg += 1
        print("{0:.3f}%".format(numAboveAvg*100/float(numStudents)))
