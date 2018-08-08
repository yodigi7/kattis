def memoize(f):
    memo = {}

    def helper(list_one: list, list_two: list, time: int):
        inp = (tuple(list_one), tuple(list_two), time)
        if inp not in memo:
            memo[inp] = f(list_one, list_two, time)
        return memo[inp]
    return helper


def get_num_times(entry_times: list, exit_times: list, likely_time: int) -> int:
    max_num_times = 0
    for i in range(len(entry_times)):
        for j in [x for x in range(len(exit_times)) if exit_times[x] - entry_times[i] is likely_time]:
            max_num_times = max(max_num_times, 1 + get_num_times(entry_times[i+1:], exit_times[j+1:], likely_time))
    return max_num_times


def main(get_num_times_function):
    input()
    input()
    entry_times = [int(x) for x in input().split()]
    exit_times = [int(x) for x in input().split()]
    likely_time = 0
    num_times = 0
    for i in range(len(entry_times)):
        for j in [x for x in range(len(exit_times)) if exit_times[x] >= entry_times[i]]:
            curr_likely_time = exit_times[j] - entry_times[i]
            curr_num_times = 1 + get_num_times_function(entry_times[i + 1:], exit_times[j + 1:], curr_likely_time)
            if curr_num_times > num_times:
                likely_time = curr_likely_time
                num_times = curr_num_times
            elif curr_num_times is num_times and curr_likely_time < likely_time:
                likely_time = curr_likely_time
    print(likely_time)


if __name__ == '__main__':
    get_num_times = memoize(get_num_times)
    main(get_num_times)
