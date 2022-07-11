def get_distance(peaks, i, j):
    if i + 1 >= j:
        return 0
    top = min(peaks[i], peaks[j])
    return top - min(peaks[i + 1 : j])


def solve_subset(peaks, start):
    pass


def solve(peaks, start):
    if len(peaks) <= 2:
        return []
    peak = peaks[start]
    temp_list = peaks[start + 1 :]
    if len(temp_list) <= 2:
        return []
    max_item = max(temp_list)
    if max_item > peak:
        try:
            next_peak = next(x for x in temp_list if x >= peak)
            j = temp_list.index(next_peak) + start + 1
        except StopIteration:
            print("This shouldn't happen")
            return []
    else:
        j = temp_list.index(max_item) + start + 1
    return solve(peaks, j).append((start, j))


if __name__ == "__main__":
    n = int(input())
    peaks = [int(x) for x in input().split()]
    print(max((get_distance(peaks, i, j) for i, j in solve(peaks, 0)), 0))
