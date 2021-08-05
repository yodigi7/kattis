mapping = {
    0: ["***", "* *", "* *", "* *", "***"],
    1: ["  *", "  *", "  *", "  *", "  *"],
    2: ["***", "  *", "***", "*  ", "***"],
    3: ["***", "  *", "***", "  *", "***"],
    4: ["* *", "* *", "***", "  *", "  *"],
    5: ["***", "*  ", "***", "  *", "***"],
    6: ["***", "*  ", "***", "* *", "***"],
    7: ["***", "  *", "  *", "  *", "  *"],
    8: ["***", "* *", "***", "* *", "***"],
    9: ["***", "* *", "***", "  *", "***"],
}


def get_next_number(arr):
    arr = [st[0:3] for st in arr]
    for key, value in mapping.items():
        if arr == value:
            return key
    return -1


def del_number(arr):
    if len(arr[0]) <= 4:
        return [[],[],[],[],[]]
    else:
        return [st[4:] for st in arr]


def main():
    arr = [input() for _ in range(5)]
    num = 0
    while len(arr[0]) >= 3:
        num *= 10
        curr_num = get_next_number(arr)
        if curr_num == -1:
            print("BOOM!!")
            return
        num += curr_num
        arr = del_number(arr)
    if num % 6 == 0:
        print("BEER!!")
    else:
        print("BOOM!!")


main()
