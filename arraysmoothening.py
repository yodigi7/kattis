# def solve(a, k):
#     a = sorted([a.count(x) for x in set(a)], reverse=True)
#     i = 0
#     length = len(a) - 1
#     for _ in range(k):
#         if i is length:
#             i = 0
#         elif a[i] < a[i + 1]:
#             i += 1
#         else:
#             i = 0
#         a[i] -= 1
#     if a[i + 1] <= a[i]:
#         return a[i]
#     else:
#         return a[i + 1]


# def solve(a, k):
#     if len(a) <= k:
#         return 0
#     a_set = set(a)
#     unique_vals = len(a_set)
#     a = sorted(list({a.count(x) for x in a_set}), reverse=True)
#     while k > 0:
#         current_sub_mult = unique_vals - len(a)
#         if len(a) > 1:
#             k = (a[0] - a[1]) * current_sub_mult
#             a = a[1:]
#             current_sub_mult += 1
#         else:
#             a[0] -= k
#     return max(0, a[0])


from collections import defaultdict


def get_count_list(a):
    temp_dict = defaultdict(lambda: 0)
    for val in a:
        temp_dict[val] += 1
    return sorted(list(temp_dict.values()), reverse=True)


def solve(a, k):
    if len(a) <= k:
        return 0
    sorted_count = get_count_list(a)
    if k == 0:
        return sorted_count[0]
    return solve_sorted_count(sorted_count, k)


def solve_sorted_count(sorted_count, k):
    sorted_diff = []
    sorted_diff_mult = []
    length = len(sorted_count) - 1
    for i, val in enumerate(sorted_count):
        if i < length:
            sorted_diff.append(val - sorted_count[i + 1])
            sorted_diff_mult.append((val - sorted_count[i + 1]) * (i + 1))
        else:
            sorted_diff.append(val)
            sorted_diff_mult.append((val) * (i + 1))
    temp_k = k
    i = -1
    while temp_k > 0:
        i += 1
        temp_k -= sorted_diff_mult[i]
    if temp_k == 0:
        return sum(sorted_diff_mult[: i + 1])
    else:
        partial = sum(sorted_diff_mult[:i])
        return (sorted_diff[i] // (i + 1)) + partial


# print(solve_sorted_count([75, 50, 25, 10, 1], 100))


if __name__ == "__main__":
    k = int(input().split()[1])
    a = input().split()

    print(solve(a, k))
