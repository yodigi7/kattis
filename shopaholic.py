def get_max_discount(item_list: list) -> int:
    item_list = list(reversed(sorted(item_list)))
    discount = 0
    for i in range(2, len(item_list), 3):
        discount += item_list[i]
    return discount


if __name__ == '__main__':
    num_items = int(input())
    print(get_max_discount([int(x) for x in input().split()]))
