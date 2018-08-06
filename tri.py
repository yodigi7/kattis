import itertools

def add(num1, num2, num3):
    if num1 + num2 == num3:
        return '+'
    return ''

def subtract(num1, num2, num3):
    if num1 - num2 == num3:
        return '-'
    return ''

def multiply(num1, num2, num3):
    if num1 * num2 == num3:
        return '*'
    return ''

def divide(num1, num2, num3):
    if num1 / num2 == num3:
        return '/'
    return ''

numbers = input().split()
numbers = [int(x) for x in numbers]
permutations = itertools.permutations(numbers, 3)
functions = [add, subtract, multiply, divide]
solved = False
for i in permutations:
    if solved:
        break
    for j in functions:
        operator = j(i[0], i[1], i[2])
        if (not operator == '') and (not i[0] == numbers[2]):
            if i[0] == numbers[1] and i[1] == numbers[2]:
                print(str(numbers[0]) + '=' + str(numbers[1]) + operator + str(numbers[2]))
                solved = True
                break
            elif i[0] == numbers[0] and i[1] == numbers[1]:
                print(str(numbers[0]) + operator + str(numbers[1]) + '=' + str(numbers[2]))
                solved = True
                break