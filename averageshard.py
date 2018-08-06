class AverageHardProblem:
    def __init__(self, cs_college_size, econ_college_size):
        self.cs_college_size = cs_college_size
        self.econ_college_size = econ_college_size
        self.cs_college_list = self.get_intelligence_list()
        self.econ_college_list = self.get_intelligence_list()
        self.cs_college_average = self.calculate_average(self.cs_college_list)
        self.econ_college_average = self.calculate_average(self.econ_college_list)

    @staticmethod
    def calculate_average(intelligence_list):
        total = 0
        for item in intelligence_list:
            total += item
        return total/len(intelligence_list)

    @staticmethod
    def get_intelligence_list():
        intel_list = input().split()
        intel_list = [int(x) for x in intel_list]
        return intel_list

    def get_solution(self):
        answer = 0
        for item in self.cs_college_list:
            if item < self.cs_college_average and item > self.econ_college_average:
                answer += 1
        return answer


if __name__ == "__main__":
    num_problems = int(input())
    for _ in range(num_problems):
        input()
        sizes = input().split()
        sizes = [int(x) for x in sizes]
        print(AverageHardProblem(sizes[0], sizes[1]).get_solution())
