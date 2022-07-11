def probable_prize(n, t):
    max_prize = 2 ** n
    probability_all_correct = (1 - t) ** n
    return max_prize * probability_all_correct


def solve(n, t):
    return max(probable_prize(i, t) for i in range(n))


if __name__ == "__main__":
    while True:
        n, t = input().split()
        n, t = int(n), float(t)
        if n == 0 and t == 0:
            break
        print(solve(n, t))
