if __name__ == '__main__':
    numCases = int(input())
    for _ in range(numCases):
        holder = input().split()
        numStudents = int(holder[0])
        grades = []
        for j in range(1, numStudents+1):
            grades.append(int(holder[j]))
        average = sum(grades)/float(numStudents)
        numAboveAvg = 0
        for grade in grades:
            if grade > average:
                numAboveAvg += 1
        print("{0:.3f}%".format(numAboveAvg*100/float(numStudents)))
