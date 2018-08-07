def coor_to_letter(coordinate: list) -> chr:
    return chr(coordinate[0]*4 + coordinate[1])


def letter_to_coor(letter: chr) -> tuple:
    x = (ord(letter)-65)//4
    y = (ord(letter)-65) % 4
    return x, y


def calculate_error(letter: chr, coordinate: list) -> int:
    ideal_coor = letter_to_coor(letter)
    return abs(ideal_coor[0] - coordinate[0]) + abs(ideal_coor[1] - coordinate[1])


def get_manhattan_distance(letter: chr, coordinate: list) -> int:
    if letter == '.' or coor_to_letter(coordinate) == letter:
        return 0
    else:
        return calculate_error(letter, coordinate)


if __name__ == '__main__':
    puzzle = [[x for x in list(input())] for _ in range(4)]
    score = 0
    for i in range(4):
        for j in range(4):
            score += get_manhattan_distance(puzzle[j][i], [j, i])
    print(score)
