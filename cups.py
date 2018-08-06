class Cup:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def __lt__(self, other):
        if self.radius < other.radius:
            return True
        return False


class CupGroup:
    def __init__(self, num_cups):
        self.cup_list = []
        self.total_cups = num_cups
        self.add_all_cups()
        self.cup_list.sort()
        self.output_solution()

    def add_all_cups(self):
        for _ in range(self.total_cups):
            self.add_next_cup()

    def add_next_cup(self):
        in_data = input().split()
        next_cup = self.create_cup(in_data)
        self.cup_list.append(next_cup)

    @staticmethod
    def create_cup(input_data):
        try:
            return Cup(int(input_data[0])/2, input_data[1])
        except ValueError:
            return Cup(int(input_data[1]),  input_data[0])

    def output_solution(self):
        for cup in self.cup_list:
            print(cup.color)


if __name__ == "__main__":
    cup_group = CupGroup(int(input()))

