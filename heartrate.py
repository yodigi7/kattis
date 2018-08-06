def solve_case():
    beats, rest = input().split()
    beats = int(beats)
    rest = float(rest)
    min_abpm = 60*(beats-1)/rest
    bpm = 60*beats/rest
    max_abpm = 60*(beats+1)/rest
    print(" ".join([str(round(min_abpm, 4)), str(round(bpm, 4)), str(round(max_abpm, 4))]))


if __name__ == '__main__':
    num_cases = int(input())
    for i in range(num_cases):
        solve_case()
