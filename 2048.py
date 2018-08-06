remMe = [0, 1, 2, 0]
matrix = [[0, 1, 2, 0], [1, 1, 2, 1], [0, 1, 2, 0], [0, 1, 2, 0]]

def move(num, list1):
    if num == 0:
        for number in range(0,3):
            list1[number] = list1[number+1]
        list1[3] = 0
    elif num == 2:
        for number in range(3,0, -1):
            list1[number] = list1[number-1]
        list1[0] = 0
    return list1

def shift(num):
    if num == 0:
        for row in range(0,4):
            if matrix[row][0] != 0 and matrix[row][1] != 0 and matrix[row][2] != 0 and matrix[row][3] != 0:
                continue
            while matrix[row][0] == 0:
                matrix[row] = move(0, matrix[row])
    elif num == 2:
        for row in range(0,4):
            if matrix[row][0] != 0 and matrix[row][1] != 0 and matrix[row][2] != 0 and matrix[row][3] != 0:
                continue
            while matrix[row][3] == 0:
                matrix[row] = move(2, matrix[row])
    elif num == 1:
        for col in range(0,4):
            if matrix[0][col] != 0 and matrix[1][col] != 0 and matrix[2][col] != 0 and matrix[3][col] != 0:
                continue
            while matrix[0][col] == 0:
                for number in range(0,3):
                    matrix[number][col] = matrix[number+1][col]
                matrix[3][col] = 0
    elif num == 3:
        for col in range(3,-1,-1):
            if matrix[0][col] != 0 and matrix[1][col] != 0 and matrix[2][col] != 0 and matrix[3][col] != 0:
                continue
            while matrix[3][col] == 0:
                for number in range(3,0,-1):
                    matrix[number][col] = matrix[number-1][col]
                matrix[0][col] = 0

def combine(num):
    if num == 0 or num == 2:
        for row in range(0,4):
            if num == 0:
                for col in range(0,3):
                    if matrix[row][col] == matrix[row][col+1]:
                        matrix[row][col] *= 2
                        for number in range(col+1,3):
                            matrix[row][col] = matrix[row][col+1]
                        matrix[row][3] = 0
            if num == 2:
                
                for col in range(3,0):
                    if matrix[row][col-1] == matrix[row][col]:
                        matrix[row][col] *= 2
                        for number in range(3,col+1,-1):
                            matrix[row][col-1] = matrix[row][col]
                        matrix[row][3] = 0
    elif num == 1 or num == 3:
        pass

'''for row in range(0,4):
    holder = input().split()
    for place in holder:
        holder[place] = int(holder[place])
    matrix[row] = holder

move = int(input())'''

num = 0
'''
while num != -1:
    num = int(input())
    remMe = move(num, remMe)
    print (remMe)
'''

while num != "-1":
    num = int(input("Input number:  "))
    shift(num)
    combine(num)
    print(matrix)
