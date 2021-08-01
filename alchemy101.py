from itertools import combinations
from functools import wraps


def cache(f):
    cache_dict = {}
    @wraps(f)
    def inner(*args):
        val = cache_dict.get(tuple(args))
        if val:
            return val
        val = f(*args)
        cache_dict[tuple(args)] = val
        return val
    return inner


@cache
def xor(num1, num2):
    return int(bin(num2), 2) ^ int(bin(num1), 2)


@cache
def solve(combination):
    if len(combination) == 1:
        return combination[0]
    total = xor(combination[0], combination[1])
    for num in combination[2:]:
        total = xor(total, num)
    return total


def main():
    for _ in range(int(input())):
        m = int(input())
        concoctions = tuple(range(1, m+1))
        solutions = []
        for i in range(m, 0, -1):
            for combination in combinations(concoctions, i):
                if solve(combination) == m:
                    solutions.append(combination)
            if solutions:
                break
        print(len(solutions[0]))
        print(" ".join(str(x) for x in solutions[0]))


main()
