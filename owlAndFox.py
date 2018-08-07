def get_closest_smaller_number(num: int) -> int:
    smaller_number = []
    str_num = str(num)
    for i in range(len(str_num) - 1, -1, -1):
        if not str_num[i] is "0":
            smaller_number.insert(0, str(int(str_num[i]) - 1))
            smaller_number = [digit for digit in str_num[:i]] + smaller_number
            break
        else:
            smaller_number.insert(0, "0")
    smaller_number = "".join(smaller_number)
    return int(smaller_number)


if __name__ == '__main__':
    num_cases = int(input())
    for _ in range(num_cases):
        print(get_closest_smaller_number(int(input())))
