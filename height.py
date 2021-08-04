def get_steps(curr, student):
    return len(curr) - curr.index(student) - 1


def solve(students):
    curr_line = []
    steps = 0
    for student in students:
        curr_line = curr_line + [student]
        curr_line.sort()
        steps += get_steps(curr_line, student)
    return steps


def main():
    for i in range(1, int(input())+1):
        solution = solve([int(x) for x in input().split()][1:])
        print(f"{i} {solution}")


main()