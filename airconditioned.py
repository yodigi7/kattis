from typing import List


def solution(minions: List[List[int]]) -> List[set]:
    rooms = []
    for minion in minions:
        minion[1] += 1
        minion_range = tuple(range(*minion))
        for i, room in enumerate(rooms):
            if not set(room).isdisjoint(minion_range):
                rooms[i] = set(room).intersection(minion_range)
                break
        else:
            rooms.append(minion_range)
    return rooms


def main():
    minions = ([int(x) for x in input().split()] for _ in range(int(input())))
    sol = solution(minions)
    # print(sol)
    print(len(sol))


if __name__ == "__main__":
    main()
