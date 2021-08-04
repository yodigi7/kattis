def is_arithmetic_seq(arr):
    if len(arr) < 2:
        return True

    diff = arr[1] - arr[0]
    for i, num in enumerate(arr):
        if i == 0:
            continue
        if arr[i] - arr[i-1] != diff:
            return False
    return True


def solve(arr):
    if is_arithmetic_seq(arr):
        return "arithmetic"
    elif is_arithmetic_seq(sorted(arr)):
        return "permuted arithmetic"
    else:
        return "non-arithmetic"


def main():
    for _ in range(int(input())):
        print(solve([int(x) for x in input().split()][1:]))


main()