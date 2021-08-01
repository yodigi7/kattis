def get_num_between(first, second, clockwise=True):
    if clockwise:
        if first < second:
            first += 40
        return first - second
    elif not clockwise:
        if first > second:
            second += 40
        return second - first

def solve(start, first, second, third):
    total_numbers = get_num_between(start, first) + get_num_between(first, second, clockwise=False) + get_num_between(second, third)
    return 1080+total_numbers*9


def main():
    while True:
        start, first, second, third = (int(x) for x in input().split())
        if not start and not first and not second and not third:
            return

        print(solve(start, first, second, third))

main()