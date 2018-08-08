def price_of_array(array: list) -> int:
    return min(array)*max(array)*len(array)


def sum_of_combinations(array: list) -> int:
    if len(array) is 0:
        return 0
    if len(array) is 1:
        return price_of_array(array)
    tot_price = 0
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)+1):
            tot_price += price_of_array(array[i:j])
            if len(str(tot_price)) > 9:
                tot_price = int(str(tot_price)[-9:])
    return tot_price


if __name__ == '__main__':
    print(
        sum_of_combinations(
            [int(input())
             for x in
             range(int(input()))]))
