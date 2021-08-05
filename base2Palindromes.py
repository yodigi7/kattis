from math import ceil


def get_len_base2_str(pos):
    curr_len = 1
    curr_pos = 1
    for _ in range(pos):
        curr_len += 1
        curr_pos += ceil(curr_len/2)
        if curr_pos >= pos:
            return curr_len


def get_pos(base2_str):
    curr_pos = 1
    for i in range(1, len(base2_str)):
        curr_pos += ceil(i/2)
    curr_pos += base2_str[:ceil(len(base2_str)/2)].count("1")
    return curr_pos - 1


def solve(pos):
    if pos == 1:
        return "1"
    len_base2_str = get_len_base2_str(pos)
    if len_base2_str % 2 == 0:
        for i in range(1, len_base2_str):
            curr_str = ("1"*i) + ("0"*((len_base2_str//2)-i))
            curr_str += curr_str[::-1]
            if get_pos(curr_str) == pos:
                return curr_str
    else:
        for i in range(1, len_base2_str):
            curr_str = ("1"*i) + ("0"*(ceil(len_base2_str/2)-i))
            curr_str += curr_str[:-1][::-1]
            if get_pos(curr_str) == pos:
                return curr_str


def main():
    pos = int(input())
    print(int(solve(pos),2))


main()