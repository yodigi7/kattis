import math

# TODO: Make it rotate the correct way so we don't have to rotate it three times
def rot90(array: list) -> list:
    return list(zip(*array[::-1]))


def solve_problem():
    encoded_message = input()
    square_size = int(math.sqrt(len(encoded_message)))
    encoded_square_message = []
    for i in range(1, square_size + 1):
        encoded_square_message.append(list(encoded_message[(i-1)*square_size:i*square_size]))
    decoded_square_message = [item for sublist in (rot90(rot90(rot90(encoded_square_message)))) for item in
                              sublist]
    print("".join(decoded_square_message))


if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        solve_problem()
