import time


def sum_of_combinations(array: list) -> int:
    start = time.time()
    dict_of_arr = {index: array[index] for index in range(len(array))}
    print(time.time() - start)
    tot_price = 0
    length_of_array = len(array)
    length_of_array_plus_one = length_of_array + 1
    for i in range(0, length_of_array):
        maxi = dict_of_arr[i]
        mini = dict_of_arr[i]
        length = 1
        for j in range(i + 1, length_of_array_plus_one):
            new_number = dict_of_arr[j - 1]
            if new_number > maxi:
                maxi = new_number
            elif new_number < mini:
                mini = new_number
            tot_price += mini*maxi*length
            length += 1
        if len(str(tot_price)) > 9:
            tot_price = int(str(tot_price)[-9:])
    print(time.time() - start)
    return tot_price


if __name__ == '__main__':
    # print(sum_of_combinations([int(input()) for x in range(int(input()))]))
    print(sum_of_combinations(list(range(10000))))
