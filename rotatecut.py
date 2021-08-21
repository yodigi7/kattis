import math


def solve(rotatecuts, message):
    for _ in range(rotatecuts):
        # Rotate and cut
        message = message[::-1][: math.ceil(len(message) * 3 / 4)]
    if rotatecuts % 2 == 1:
        # Flip again if ended up backwards
        return message[::-1]
    return message


def main():
    for _ in range(int(input())):
        rotatecuts, message = input().split()
        rotatecuts = int(rotatecuts)
        print(solve(rotatecuts, message))


main()
