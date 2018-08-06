class Musician:
    def __init__(self, name):
        self.name = name

    def __lt__(self, other):
        if self.name[0] < other.name[0]:
            return True
        elif self.name[0] > other.name[0]:
            return False
        elif self.name[1] < other.name[1]:
            return True
        elif self.name[1] > other.name[1]:
            return False
        else:
            return False


if __name__ == "__main__":
    num_musicians = int(input())
    musicians_list = []
    while num_musicians:
        for i in range(num_musicians):
            musicians_list.append(Musician(input()))
        musicians_list = sorted(musicians_list)
        for musician in musicians_list:
            print(musician.name)
        musicians_list = []
        num_musicians = int(input())
        print()
