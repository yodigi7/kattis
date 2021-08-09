from itertools import combinations
flip_dict = {
    "1": "1",
    "2": "2",
    "5": "5",
    "6": "9",
    "8": "8",
    "9": "6",
    "0": "0",
}


def flippable(num):
    return all(x in flip_dict for x in str(num))


def flip(num):
    return int("".join(flip_dict[x] for x in reversed(str(num))))


def solve(target, numbers):
    for combination in combinations(numbers, 2):
        if combination[0] + combination[1] == target:
            return "YES"
        if flippable(combination[0]) and flip(combination[0]) + combination[1] == target:
            return "YES"
        if flippable(combination[1]) and flip(combination[1]) + combination[0] == target:
            return "YES"
        if flippable(combination[1]) and flippable(combination[0]) and flip(combination[1]) + flip(combination[0]) == target:
            return "YES"
    return "NO"


def main():
    n, s = [int(x) for x in input().split()]
    numbers = {int(x) for x in input().split()}
    print(solve(s, numbers))


main()