def path_to_number(path: list):
    holder = 1
    for dir in path:
        if dir == 'L':
            holder *= 2
        elif dir == 'R':
            holder *= 2
            holder += 1
    return holder


def get_end_number(root_number: int, path: list):
    return root_number - path_to_number(path)


if __name__ == '__main__':
    inp = input().split()
    tree_height = int(inp[0])
    try:
        path = list(inp[1])
    except IndexError:
        path = []
    root_number = 2**(tree_height + 1)
    print(get_end_number(root_number, path))
