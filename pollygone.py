import math
from itertools import combinations


def find_solution_n_boxes(box_list, max_boxes, necessary_probability):
    all_possible_combinations = combinations(box_list, max_boxes)

    best_solution = math.inf
    for combination in all_possible_combinations:
        sum_prob = 0
        sum_effort = 0
        for box in combination:
            sum_prob += box.probability
            sum_effort += box.effort
        if sum_prob >= necessary_probability:
            best_solution = min(best_solution, sum_effort)
    return best_solution


def find_solution(box_list, necessary_probability):
    num_boxes = len(box_list)

    best_solution = math.inf
    for n in range(1, num_boxes+1):
        solution = find_solution_n_boxes(box_list, n, necessary_probability)
        best_solution = min(best_solution, solution)

    return best_solution


class Box:
    def __init__(self, effort, probability):
        self.effort = effort
        self.probability = probability

    def __str__(self):
        return str((self.effort, self.probability))

    def __repr__(self):
        return str((self.effort, self.probability))


if __name__ == "__main__":
    line = input().split()
    num_boxes = int(line[0])
    min_effort_prob = float(line[1])
    box_list = []

    for _ in range(num_boxes):
        line = input().split()
        effort = int(line[0])
        probability = float(line[1])
        box_list.append(Box(effort, probability))

    print(find_solution(box_list, min_effort_prob))
