from itertools import combinations_with_replacement
from operator import add, mul, sub, floordiv

text_mapping = {
    0: "+",
    1: "-",
    2: "*",
    3: "/",
}
mapping = {
    0: add,
    1: sub,
    2: mul,
    3: floordiv,
}


def partial_solve(nums, fns, mult_or_div=True):
    if mult_or_div:
        while mul in fns or floordiv in fns:
            for i, fn in enumerate(fns):
                if fn is mul or fn is floordiv:
                    nums[i] = fn(nums[i], nums[i+1])
                    del nums[i+1]
                    del fns[i]
                    break
    else:
        while sub in fns or add in fns:
            for i, fn in enumerate(fns):
                if fn is sub or fn is add:
                    nums[i] = fn(nums[i], nums[i+1])
                    del nums[i+1]
                    del fns[i]
                    break
    return nums, fns


def apply(fns):
    nums = [4]*4
    copy_fns = [x for x in fns]
    nums, copy_fns = partial_solve(nums, copy_fns)
    return partial_solve(nums, copy_fns, False)[0][0]


def find_sol(target):
    for combination in combinations_with_replacement(mapping.keys(), 3):
        x, y, z = combination
        mapped_combination = mapping[x], mapping[y], mapping[z]
        if apply(mapped_combination) == target:
            return combination
    return None



def main():
    for _ in range(int(input())):
        target = int(input())
        res = find_sol(target)
        if res:
            x, y, z = res
            print(f"4 {text_mapping[x]} 4 {text_mapping[y]} 4 {text_mapping[z]} 4 = {target}")
        else:
            print("no solution")


main()