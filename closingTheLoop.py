def solution():
    input()
    segments = input().split()
    red_segs = list(reversed(sorted([int(x[:-1]) for x in segments if x[-1:] == 'R'])))
    blue_segs = list(reversed(sorted([int(x[:-1]) for x in segments if x[-1:] == 'B'])))
    min_len = min(len(red_segs), len(blue_segs))
    return (sum(red_segs[:min_len]) + sum(blue_segs[:min_len])) - min_len*2


if __name__ == '__main__':
    num_cases = int(input())
    for case_num in range(1, num_cases + 1):
        print("Case #{}: {}".format(case_num, solution()))
