def get_possibilites(second_dim: int) -> int:
    if second_dim % 2 is 1:
        return 0
    elif second_dim is 0:
        return 1
    elif second_dim is 2:
        return 3
    else:
        return 4*get_possibilites(second_dim-2) - get_possibilites(second_dim-4)


if __name__ == '__main__':
    inp = int(input())
    while inp >= 0:
        print(get_possibilites(inp))
        inp = int(input())
