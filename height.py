from copy import deepcopy


def get_problem_data():
    problem_data = input().split()
    problem_data.pop(0)
    return problem_data


class HeightProblem:
    def __init__(self, index, problem_data):
        self.index = index
        self.problem_data = problem_data
        self.steps_back = 0
        self.line = []

    def steps_back_all(self):
        self.line = [self.problem_data[0]]
        self.problem_data.pop(0)
        for _ in range(len(self.problem_data)):
            number = self.problem_data[0]
            self.problem_data.pop(0)
            insert_index = self.find_index_in_line(number)
            self.steps_back += (len(self.line)-insert_index)
            self.line.insert(insert_index, number)

    def find_index_in_line(self, number):
        for list_index in range(len(self.line)):
            if self.line[list_index] > number:
                return list_index
        return len(self.line)

    def output_solution(self):
        print("{} {}".format(self.index+1, self.steps_back))


if __name__ == "__main__":
    number_of_data_sets = int(input())
    for index in range(number_of_data_sets):
        problem_data = get_problem_data()
        problem_instance = HeightProblem(index, problem_data)
        problem_instance.steps_back_all()
        problem_instance.output_solution()
