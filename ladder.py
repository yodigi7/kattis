import math


def get_problem_input():
    return [int(x) for x in input().split()]


def get_answer(problem_input):
    angle_in_degrees = math.radians(problem_input[1])
    exact_height = (problem_input[0])/math.sin(angle_in_degrees)
    return math.ceil(exact_height)


def output_answer(answer):
    print(answer)


if __name__ == "__main__":
    problem_input = get_problem_input()
    answer = get_answer(problem_input)
    output_answer(answer)