import itertools


def price_of_array(array: list) -> int:
    return min(array)*max(array)*len(array)


def get_remaining(combination: list, array: list):
    copy_arr = array[:]
    copy_comb = combination[:]
    while len(copy_comb) > 0:
        copy_arr.remove(copy_comb[0])
        copy_comb.remove(copy_comb[0])
    return copy_arr


def sum_of_combinations(array: list) -> int:
    if len(array) is 0:
        return 0
    if len(array) is 1:
        return price_of_array(array)
    tot_price = 0
    for i in range(1, len(array) + 1):
        combinations = [list(x) for x in itertools.combinations(array, i)]
        for combination in combinations:
            tot_price += price_of_array(combination)
            print("Sum of combinations for array: {} is {}".format(combination, tot_price))
    return tot_price


if __name__ == '__main__':
    num_items = int(input())
    array = [int(input()) for x in range(num_items)]
    print(sum_of_combinations(array))
