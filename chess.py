def letter_to_num(letter) -> int:
    return ord(letter) - ord("A") + 1


def num_to_letter(num: int) -> str:
    return chr(num + ord("A") - 1)


def valid_tuple(tup: tuple[int, int]) -> bool:
    return 0 < tup[0] < 9 and 0 < tup[1] < 9


def solve(pos1: tuple, pos2: tuple) -> str:
    if sum(pos1) % 2 != sum(pos2) % 2:
        return "Impossible"
    if pos1[0] == pos2[0] and pos1[1] == pos2[1]:
        return f"0 {num_to_letter(pos1[0])} {pos1[1]}"
    diff1 = pos1[0] - pos1[1]
    diff2 = pos2[0] - pos2[1]
    super_diff = (diff1 - diff2) // 2
    middle_pos = None
    if diff1 > diff2:
        middle_pos = pos1[0] - super_diff, pos1[1] + super_diff
    elif diff1 < diff2:
        middle_pos = pos1[0] + super_diff, pos1[1] - super_diff
    if not valid_tuple(middle_pos):
        sum1 = pos1[0] - pos1[1]
        sum2 = pos2[0] - pos2[1]
        super_diff = (sum1 - sum2) // 2
        if sum1 > sum2:
            middle_pos = pos1[0] - super_diff, pos1[1] - super_diff
        elif sum1 < sum2:
            middle_pos = pos1[0] + super_diff, pos1[1] + super_diff
    if middle_pos[0] == pos2[0] and middle_pos[1] == pos2[1]:
        return (
            f"1 {num_to_letter(pos1[0])} {pos1[1]} {num_to_letter(pos2[0])} {pos2[1]}"
        )
    return f"2 {num_to_letter(pos1[0])} {pos1[1]} {num_to_letter(middle_pos[0])} {middle_pos[1]} {num_to_letter(pos2[0])} {pos2[1]}"


if __name__ == "__main__":
    for _ in range(int(input())):
        pos1_letter, pos1_num, pos2_letter, pos2_num = input().split()
        pos1_num, pos2_num = int(pos1_num), int(pos2_num)
        pos1 = letter_to_num(pos1_letter), pos1_num
        pos2 = letter_to_num(pos2_letter), pos2_num
        print(solve(pos1, pos2))
